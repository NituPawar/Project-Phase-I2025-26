from flask import Flask, request, render_template, redirect, session, flash, url_for, send_from_directory, Response, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import os
import re
import csv
from io import StringIO

# expose Google Maps API key to templates (set env var GOOGLE_MAPS_API_KEY)
app = Flask(__name__)
app.secret_key = 'saurabh'  # replace with env var in production

# expose Google Maps API key to templates (set env var GOOGLE_MAPS_API_KEY)
@app.context_processor
def inject_google_maps_key():
    return dict(GOOGLE_MAPS_API_KEY=os.environ.get('GOOGLE_MAPS_API_KEY', ''))

# ---------- helper: human time difference ----------
def time_ago(dt):
    if not dt:
        return ''
    now = datetime.now()
    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
        dt = dt.replace(tzinfo=None)
    diff = now - dt
    seconds = diff.total_seconds()
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minutes ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hours ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} days ago"
    else:
        weeks = int(seconds / 604800)
        return f"{weeks} weeks ago"

app.jinja_env.filters['time_ago'] = time_ago

# ---------- MongoDB config ----------
# IMPORTANT: include the database name at the end of the URI.
# In production, move credentials to environment variables.
app.config['MONGO_URI'] = "mongodb+srv://suhaninaidu2003_db_user:suhani%40123@jamasya.mzm5dyx.mongodb.net/jamasya_db?retryWrites=true&w=majority"
mongo = PyMongo(app)
issues_collection = mongo.db.issues
users_collection = mongo.db.users

# ---------- uploads ----------
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# Serve the Gemini-generated hero image from workspace root at a stable route
@app.route('/hero-image.png')
def hero_image():
    # Keep the route for backward compatibility but redirect to the static URL
    return redirect(url_for('static', filename='images/Gemini_image.png'))

@app.context_processor
def utility_functions():
    def upload_url(filename):
        if not filename:
            return ''
        return url_for('uploaded_file', filename=filename)
    return dict(upload_url=upload_url)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# ---------- auth requirement ----------
@app.before_request
def require_login():
    # allow static, login, register, index, uploads and favicon without login
    allowed_routes = {
        'login', 'register', 'index', 'static', 'uploaded_file', 'favicon.ico', 'hero_image'
    }
    endpoint = request.endpoint
    if endpoint not in allowed_routes and 'user_id' not in session:
        return redirect(url_for('login'))

# ---------- routes ----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        try:
            user = users_collection.find_one({'_id': ObjectId(session['user_id'])})
        except Exception:
            user = None
        return render_template('home.html', user=user)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        raw_password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        is_admin_flag = request.form.get('is_admin')

        # convert is_admin to boolean (checkbox typically returns 'on')
        is_admin = True if is_admin_flag in ('on', 'true', '1') else False

        # Basic required fields check
        if not name or not email or not raw_password or not confirm_password or not phone or not address:
            flash('Please fill all required fields.', 'danger')
            return redirect(url_for('register'))

        # Password confirmation
        if raw_password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        # Phone validation: 10 digits starting with 7,8,9
        if not re.fullmatch(r'^[789]\d{9}$', phone):
            flash('Phone number must be 10 digits and start with 7, 8, or 9.', 'danger')
            return redirect(url_for('register'))

        # Ensure email uniqueness
        if users_collection.find_one({'email': email}):
            flash('User already exists!', 'error')
            return redirect(url_for('register'))

        password = generate_password_hash(raw_password)
        users_collection.insert_one({
            'name': name,
            'email': email,
            'password': password,
            'phone': phone,
            'address': address,
            'is_admin': is_admin
        })
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['email'] = user['email']
            # ensure boolean
            session['is_admin'] = bool(user.get('is_admin', False))
            if session['is_admin']:
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('home'))
        else:
            flash('Invalid credentials!', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/report-issue', methods=['GET', 'POST'])
def report_issue():
    # get current user's stored address (if any) to offer as an option
    profile_address = ''
    try:
        if 'user_id' in session:
            u = users_collection.find_one({'_id': ObjectId(session.get('user_id'))})
            if u:
                profile_address = u.get('address', '')
    except Exception:
        profile_address = ''

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        category = request.form.get('category', '').strip()
        location_description = request.form.get('location_description', '').strip()
        latitude_raw = request.form.get('latitude', '').strip()
        longitude_raw = request.form.get('longitude', '').strip()
        location_mode = request.form.get('location_mode', 'new')
        # normalize urgency to lowercase
        urgency_raw = request.form.get('urgency', '').strip()
        urgency = urgency_raw.lower() if urgency_raw else ''

        # server-side validation: allow alphanumeric, spaces, common punctuation, 5-100 chars
        if not re.fullmatch(r'[A-Za-z0-9\s,\.\-()]{5,100}', title):
            flash('Title must be 5–100 characters and can include letters, numbers and , . - ( )', 'danger')
            return render_template('report_issue.html', title=title, description=description, urgency=urgency, profile_address=profile_address)

        # validate urgency is selected (use lowercase)
        if not urgency or urgency not in ['low', 'medium', 'high']:
            flash('Please select an urgency level.', 'danger')
            return render_template('report_issue.html', title=title, description=description, urgency=urgency, profile_address=profile_address)

        if not description or len(description) < 10:
            flash('Description must be at least 10 characters.', 'danger')
            return render_template('report_issue.html', title=title, description=description, urgency=urgency, profile_address=profile_address)

        # category must be selected
        if not category:
            flash('Please select a category for the issue.', 'danger')
            return render_template('report_issue.html', title=title, description=description, urgency=urgency, profile_address=profile_address)

        # Location description: ensure it has some minimal length
        if not location_description or len(location_description) < 5:
            flash('Please provide a location description or pin a precise location on the map.', 'danger')
            return render_template('report_issue.html', title=title, description=description, urgency=urgency, profile_address=profile_address)

        try:
            user_obj_id = ObjectId(session.get('user_id'))
        except Exception:
            flash('Session invalid. Please login again.', 'danger')
            return redirect(url_for('login'))

        # Handle file uploads
        photo_filenames = []
        if 'photos' in request.files:
            photos = request.files.getlist('photos')
            for photo in photos:
                if photo and photo.filename and allowed_file(photo.filename):
                    filename = secure_filename(photo.filename)
                    # Add timestamp to filename to avoid conflicts
                    filename = f"{datetime.utcnow().timestamp()}_{filename}"
                    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    photo_filenames.append(filename)

        # parse lat/lng safely
        latitude = None
        longitude = None
        try:
            latitude = float(latitude_raw) if latitude_raw else None
        except Exception:
            latitude = None
        try:
            longitude = float(longitude_raw) if longitude_raw else None
        except Exception:
            longitude = None

        now = datetime.utcnow()

        issue = {
            'title': title,
            'description': description,
            'category': category,
            'location_description': location_description,
            'latitude': latitude,
            'longitude': longitude,
            'location_mode': location_mode,
            'urgency': urgency,
            'user_id': user_obj_id,
            'reporter_email': session.get('email'),
            'reporter_name': None,
            'status': 'Open',
            'read': False,
            'assigned_group': None,
            'created_at': now,
            'photo_filenames': photo_filenames if photo_filenames else [],
            'actions': []
        }
        # attach reporter name if available
        try:
            u = users_collection.find_one({'_id': ObjectId(session.get('user_id'))}) if session.get('user_id') else None
            if u and u.get('name'):
                issue['reporter_name'] = u.get('name')
        except Exception:
            pass
        # add initial action entry
        try:
            issue['actions'].append({'actor': session.get('email') or issue.get('reporter_name') or 'User', 'action': 'Reported', 'timestamp': now})
        except Exception:
            pass
        issues_collection.insert_one(issue)
        flash('Issue reported successfully.', 'success')
        return redirect(url_for('my_issues'))

    return render_template('report_issue.html', profile_address=profile_address)

@app.route('/my_issues')
def my_issues():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        user_obj = ObjectId(session['user_id'])
    except Exception:
        flash('Session invalid. Please login again.', 'danger')
        return redirect(url_for('login'))

    user_issues = list(issues_collection.find({'user_id': user_obj}).sort('created_at', -1))
    return render_template('my_issues.html', issues=user_issues)

@app.route('/all-issues')
def all_issues():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    issues = list(issues_collection.find().sort('created_at', -1))
    # Add author info to each issue (safe handling if missing user_id)
    for issue in issues:
        try:
            user = users_collection.find_one({'_id': issue.get('user_id')}) if issue.get('user_id') else None
        except Exception:
            user = None
        issue['author'] = user if user else {'name': 'Unknown'}
    return render_template('all_issues.html', issues=issues)

@app.route('/admin/all-issues', methods=['GET', 'POST'])
def admin_all_issues():
    if 'user_id' in session and session.get('is_admin'):
        if request.method == 'POST':
            issue_id = request.form.get('issue_id')
            group = request.form.get('group')
            if issue_id and group:
                try:
                    # set assigned group and record an action so action history includes assigned_group
                    actor = session.get('email') or 'admin'
                    now = datetime.utcnow()
                    issues_collection.update_one(
                        {'_id': ObjectId(issue_id)},
                        {
                            '$set': {'assigned_group': group},
                            '$push': {'actions': {'actor': actor, 'action': f'Assigned to {group}', 'assigned_group': group, 'timestamp': now}}
                        }
                    )
                    flash('Group assigned.', 'success')
                except Exception:
                    flash('Invalid issue id.', 'danger')
            # preserve filter if present
            referer_user = request.args.get('user_id')
            if referer_user:
                return redirect(url_for('admin_all_issues') + f"?user_id={referer_user}")
            return redirect(url_for('admin_all_issues'))

        # optionally filter by user_id query param
        user_id_filter = request.args.get('user_id')
        query = {}
        if user_id_filter:
            try:
                query['user_id'] = ObjectId(user_id_filter)
            except Exception:
                # invalid user id — ignore filter
                query = {}

        issues = list(issues_collection.find(query).sort('created_at', -1))
        # Add author info to each issue
        for issue in issues:
            try:
                user = users_collection.find_one({'_id': issue.get('user_id')}) if issue.get('user_id') else None
            except Exception:
                user = None
            issue['author'] = user if user else {'name': 'Unknown'}

        return render_template('admin_all_issues.html', issues=issues)

    return redirect(url_for('login'))

@app.route('/issue/<issue_id>')
def view_issue(issue_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        issue = issues_collection.find_one({'_id': ObjectId(issue_id)})
    except Exception:
        flash('Invalid issue ID', 'error')
        return redirect(url_for('my_issues'))

    if not issue:
        flash('Issue not found', 'error')
        return redirect(url_for('my_issues'))

    return render_template('view_issue.html', issue=issue)


@app.route('/issue/<issue_id>/json')
def view_issue_json(issue_id):
    # Return a compact JSON representation of the issue for polling by the UI
    try:
        issue = issues_collection.find_one({'_id': ObjectId(issue_id)})
    except Exception:
        return jsonify({'error': 'invalid id'}), 400
    if not issue:
        return jsonify({'error': 'not found'}), 404

    # Convert action timestamps to ISO strings and include assigned_group
    actions = []
    for a in issue.get('actions', []):
        ts = a.get('timestamp')
        if isinstance(ts, datetime):
            ts = ts.isoformat()
        actions.append({
            'actor': a.get('actor'),
            'action': a.get('action'),
            'assigned_group': a.get('assigned_group') if 'assigned_group' in a else None,
            'timestamp': ts
        })

    # Sort actions by timestamp descending
    actions = sorted(actions, key=lambda x: x['timestamp'] or '', reverse=True)

    return jsonify({
        'status': issue.get('status'),
        'assigned_group': issue.get('assigned_group'),
        'actions': actions
    })

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        try:
            user = users_collection.find_one({'_id': ObjectId(session['user_id'])})
        except Exception:
            user = None

        # compute unread notifications count
        try:
            user_notifs = user.get('notifications', []) if user else []
            unread_count = sum(1 for n in user_notifs if not n.get('read'))
        except Exception:
            unread_count = 0

        # Calculate stats
        try:
            reported_issues = issues_collection.count_documents({'user_id': ObjectId(session['user_id'])})
        except Exception:
            reported_issues = 0

        try:
            assigned_tasks = issues_collection.count_documents({'assigned_to': ObjectId(session['user_id'])})
        except Exception:
            assigned_tasks = 0

        resolved_issues_count = issues_collection.count_documents({'user_id': ObjectId(session['user_id']), 'status': 'Resolved'})
        community_rank = 42  # Placeholder

        stats = {
            'reported_issues': reported_issues,
            'assigned_tasks': assigned_tasks,
            'resolved_issues': resolved_issues_count,
            'community_rank': community_rank
        }

        # placeholder lists (you can replace with real queries)
        recent_activities = [
            {'icon': 'plus-circle', 'description': 'Reported a new issue', 'timestamp': datetime.utcnow()},
            {'icon': 'check-circle', 'description': 'Issue resolved', 'timestamp': datetime.utcnow()},
        ]

        priority_issues = [
            {'id': '123', 'title': 'Pothole on Main St', 'priority': 'high', 'progress': 75, 'status': 'in-progress', 'type': 'reported'},
            {'id': '124', 'title': 'Broken streetlight', 'priority': 'medium', 'progress': 40, 'status': 'pending', 'type': 'assigned'},
        ]

        trending_issues = [
            {'id': '125', 'title': 'Garbage accumulation', 'comments': 5},
            {'id': '126', 'title': 'Water leakage', 'comments': 3},
        ]

        resolved_issues = [
            {'id': '127', 'title': 'Road repair', 'resolved_at': datetime.utcnow()},
            {'id': '128', 'title': 'Park maintenance', 'resolved_at': datetime.utcnow()},
        ]

        return render_template('dashboard.html', user=user, unread_count=unread_count, stats=stats,
                               recent_activities=recent_activities, priority_issues=priority_issues,
                               trending_issues=trending_issues, resolved_issues=resolved_issues)
    return redirect(url_for('login'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' in session and session.get('is_admin'):
        issues = list(issues_collection.find().sort('created_at', -1))
        # add stringified user id for client-side use
        for issue in issues:
            try:
                issue['user_id_str'] = str(issue.get('user_id')) if issue.get('user_id') else ''
            except Exception:
                issue['user_id_str'] = ''
        # fetch users and attach their issues count
        users = list(users_collection.find())
        for u in users:
            try:
                u['_id_str'] = str(u.get('_id'))
                u['issue_count'] = issues_collection.count_documents({'user_id': u.get('_id')})
            except Exception:
                u['_id_str'] = ''
                u['issue_count'] = 0
        # Calculate statistics for charts - expect urgency stored as 'low'|'medium'|'high'
        urgency_counts = {'low': 0, 'medium': 0, 'high': 0}
        status_counts = {'Open': 0, 'Resolved': 0}
        for issue in issues:
            urgency = (issue.get('urgency') or 'low').lower()
            status = issue.get('status', 'Open')
            urgency_counts[urgency] = urgency_counts.get(urgency, 0) + 1
            status_counts[status] = status_counts.get(status, 0) + 1
        return render_template('admin_dashboard.html', issues=issues,
                       urgency_counts=urgency_counts, status_counts=status_counts,
                       users=users)
    return redirect(url_for('login'))

@app.route('/notifications/mark_all_read', methods=['POST'])
def mark_all_read():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    try:
        user = users_collection.find_one({'_id': ObjectId(session['user_id'])})
    except Exception:
        user = None
    if user:
        notifs = user.get('notifications', [])
        for n in notifs:
            n['read'] = True
        users_collection.update_one({'_id': ObjectId(session['user_id'])}, {'$set': {'notifications': notifs}})
    return redirect(url_for('notifications'))

# ------------- admin exports / actions -------------
@app.route('/admin/export_issues')
def export_issues():
    if 'user_id' in session and session.get('is_admin'):
        issues = list(issues_collection.find().sort('created_at', -1))
        si = StringIO()
        cw = csv.writer(si)
        # Write header (include more fields to export full issue details)
        cw.writerow(['Issue ID', 'Title', 'Description', 'Category', 'Location', 'Latitude', 'Longitude', 'Urgency', 'Status', 'Read', 'Reporter Name', 'Reporter Email', 'Created At'])
        for issue in issues:
            cw.writerow([
                str(issue.get('_id')),
                issue.get('title', ''),
                issue.get('description', ''),
                issue.get('category', ''),
                issue.get('location_description', ''),
                issue.get('latitude', ''),
                issue.get('longitude', ''),
                issue.get('urgency', ''),
                issue.get('status', ''),
                'Yes' if issue.get('read') else 'No',
                issue.get('reporter_name', ''),
                issue.get('reporter_email', ''),
                issue.get('created_at').strftime('%Y-%m-%d %H:%M') if issue.get('created_at') else ''
            ])
        output = si.getvalue()
        return Response(
            output,
            mimetype='text/csv',
            headers={"Content-Disposition": "attachment;filename=issues_export.csv"}
        )
    return redirect(url_for('login'))

@app.route('/admin/mark_read/<issue_id>', methods=['POST'])
def mark_read(issue_id):
    if 'user_id' in session and session.get('is_admin'):
        try:
            actor = session.get('email') or 'admin'
            now = datetime.utcnow()
            issues_collection.update_one(
                {'_id': ObjectId(issue_id)},
                {
                    '$set': {'read': True},
                    '$push': {'actions': {'actor': actor, 'action': 'Marked as Read', 'timestamp': now}}
                }
            )
        except Exception:
            flash('Invalid issue id', 'danger')
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('login'))

@app.route('/admin/set_urgency/<issue_id>', methods=['POST'])
def set_urgency(issue_id):
    if 'user_id' in session and session.get('is_admin'):
        urgency = (request.form.get('urgency') or '').lower()
        if urgency in ['low', 'medium', 'high']:
            try:
                actor = session.get('email') or 'admin'
                now = datetime.utcnow()
                issues_collection.update_one(
                    {'_id': ObjectId(issue_id)},
                    {
                        '$set': {'urgency': urgency},
                        '$push': {'actions': {'actor': actor, 'action': f"Set urgency to {urgency.title()}", 'timestamp': now}}
                    }
                )
            except Exception:
                flash('Invalid issue id', 'danger')
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('login'))

@app.route('/admin/resolve_issue/<issue_id>', methods=['POST'])
def resolve_issue(issue_id):
    if 'user_id' in session and session.get('is_admin'):
        try:
            actor = session.get('email') or 'admin'
            now = datetime.utcnow()
            # mark resolved and record action
            issues_collection.update_one(
                {'_id': ObjectId(issue_id)},
                {
                    '$set': {'status': 'Resolved'},
                    '$push': {'actions': {'actor': actor, 'action': 'Marked as Resolved', 'timestamp': now}}
                }
            )
            # create a user-facing notification if the issue has an owner
            issue = issues_collection.find_one({'_id': ObjectId(issue_id)})
            if issue and issue.get('user_id'):
                try:
                    user_id = issue.get('user_id')
                    title = issue.get('title', 'your issue')
                    notif = {
                        'issue_id': str(issue_id),
                        'message': f'🎉 Congratulations! Your issue "{title}" has been resolved.',
                        'timestamp': now,
                        'read': False
                    }
                    users_collection.update_one({'_id': user_id}, {'$push': {'notifications': notif}})
                except Exception:
                    # don't fail the whole request if notification can't be saved
                    pass
        except Exception:
            flash('Invalid issue id', 'danger')
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('login'))


@app.route('/admin/set_status/<issue_id>', methods=['POST'])
def set_status(issue_id):
    if 'user_id' in session and session.get('is_admin'):
        status = (request.form.get('status') or '').strip()
        # normalize status: allow 'Open', 'In Progress', 'Pending', 'Resolved'
        allowed = {'Open', 'In Progress', 'Pending', 'Resolved'}
        if status not in allowed:
            flash('Invalid status selected.', 'danger')
            return redirect(request.referrer or url_for('admin_all_issues'))
        try:
            actor = session.get('email') or 'admin'
            now = datetime.utcnow()
            issues_collection.update_one(
                {'_id': ObjectId(issue_id)},
                {
                    '$set': {'status': status},
                    '$push': {'actions': {'actor': actor, 'action': f'Set status to {status}', 'timestamp': now}}
                }
            )
            # If the status became Resolved, create a user notification
            if status == 'Resolved':
                try:
                    issue = issues_collection.find_one({'_id': ObjectId(issue_id)})
                    if issue and issue.get('user_id'):
                        title = issue.get('title', 'your issue')
                        notif = {
                            'issue_id': str(issue_id),
                            'message': f'🎉 Congratulations! Your issue "{title}" has been resolved.',
                            'timestamp': now,
                            'read': False
                        }
                        users_collection.update_one({'_id': issue.get('user_id')}, {'$push': {'notifications': notif}})
                except Exception:
                    pass

            flash(f'Status updated to {status}', 'success')
        except Exception:
            flash('Invalid issue id', 'danger')
        return redirect(request.referrer or url_for('admin_all_issues'))
    return redirect(url_for('login'))

@app.route('/admin/delete_issue/<issue_id>', methods=['POST'])
def delete_issue(issue_id):
    if 'user_id' in session and session.get('is_admin'):
        try:
            issues_collection.delete_one({'_id': ObjectId(issue_id)})
        except Exception:
            flash('Invalid issue id', 'danger')
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('login'))

# ---------- run ----------
if __name__ == '__main__':
    app.run(debug=True, port=50002)
