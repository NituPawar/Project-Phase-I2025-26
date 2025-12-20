from flask import Flask, send_from_directory, url_for, render_template
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

# If you store uploaded images outside the static folder, add a route to serve them:
# (optional) serve files from 'uploads' directory inside project root
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return render_template('blog_post.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@app.route('/rss')
def rss():
    return render_template('rss.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/privacy')
def privacy():  
