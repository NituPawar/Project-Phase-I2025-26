from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
import pandas as pd
from fuzzywuzzy import process
import threading
import webbrowser

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace with a secure key

# ------------------- MongoDB Setup -------------------
client = MongoClient('mongodb://localhost:27017/')
db = client['Ayurveda']
users_collection = db['User']

# ------------------- ML MODEL & DATASET SETUP -------------------
df = pd.read_csv('dataset.csv', encoding='cp1252')
df['remedy_label'] = df['remedy'].astype('category').cat.codes
remedy_categories = df['remedy'].astype('category').cat.categories

vectorizer = joblib.load('vectorizer.joblib')
model = joblib.load('model.joblib')

known_symptoms = df['symptoms'].unique()

def correct_symptom(input_symptom):
    match, score = process.extractOne(input_symptom, known_symptoms)
    if score >= 70:
        return match
    return None

# ---------------------- Routes ----------------------
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symptoms_input = data.get('symptoms', '').strip()

    if not symptoms_input:
        return jsonify({'error': 'Please enter symptoms.'}), 400

    symptoms_list = [s.strip() for s in symptoms_input.split(',') if s.strip()]

    if not symptoms_list:
        return jsonify({'error': 'No valid symptoms provided.'}), 400

    remedies = []
    for raw_symptom in symptoms_list:
        corrected = correct_symptom(raw_symptom)
        if corrected:
            X_test = vectorizer.transform([corrected])
            pred_label = model.predict(X_test)[0]
            remedy = remedy_categories[pred_label]
            remedies.append({
                'input': raw_symptom,
                'corrected': corrected,
                'remedy': remedy
            })
        else:
            remedies.append({
                'input': raw_symptom,
                'error': 'Symptom not recognized'
            })

    return jsonify({'results': remedies})

# ---------------------- Registration & Login ----------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if users_collection.find_one({'email': email}):
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(password)
        users_collection.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password
        })

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            session['email'] = user['email']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# ---------------------- Symptom Page for PDF Generation ----------------------
@app.route('/symptom')
def symptom():
    # Pass username from session to template
    username = session.get('username', 'Guest')
    return render_template('symptom.html', username=username)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aloe-vera')
def aloe_vera():
    return render_template('aloe-vera.html')

@app.route('/amla')
def amla():
    return render_template('amla.html')

@app.route('/ashwagandha')
def ashwagandha():
    return render_template('ashwagandha.html')

@app.route('/liver')
def liver():
    return render_template('liver.html')

@app.route('/bael')
def bael():
    return render_template('bael.html')

@app.route('/pregnancy')
def pregnancy():
    return render_template('pregnancy.html')


@app.route('/brahmi')
def brahmi():
    return render_template('brahmi.html')

@app.route('/cancer')
def cancer():
    return render_template('cancer.html')

@app.route('/cinnamon')
def cinnamon():
    return render_template('cinnamon.html')

@app.route('/clove')
def clove():
    return render_template('clove.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/curry-leaves')
def curry_leaves():
    return render_template('curry-leaves.html')

@app.route('/digestion')
def digestion():
    return render_template('digestion.html')

@app.route('/reproduction')
def reproduction():
    return render_template('reproduction.html')

@app.route('/eye')
def eye():
    return render_template('eye.html')

@app.route('/sleep')
def sleep():
    return render_template('sleep.html')

@app.route('/fenugreek')
def fenugreek():
    return render_template('fenugreek.html')

@app.route('/garlic')
def garlic():
    return render_template('garlic.html')

@app.route('/ginger')
def ginger():
    return render_template('ginger.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/bone')
def bone():
    return render_template('bone.html')

@app.route('/stress')
def stress():
    return render_template('stress.html')

@app.route('/hibiscus')
def hibiscus():
    return render_template('hibiscus.html')

@app.route('/hormonal')
def hormonal():
    return render_template('hormonal.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/joint_pain')
def joint_pain():
    return render_template('joint_pain.html')

@app.route('/lemon')
def lemon():
    return render_template('lemon.html')


@app.route('/fever')
def fever():
    return render_template('fever.html')

@app.route('/immunity')
def immunity():
    return render_template('immunity.html')

@app.route('/oral')
def oral():
    return render_template('oral.html')



@app.route('/mental')
def mental():
    return render_template('mental.html')

@app.route('/mint')
def mint():
    return render_template('mint.html')

@app.route('/neem')
def neem():
    return render_template('neem.html')

@app.route('/diabetes')
def diabetes():
    # your code here
    return render_template('diabetes.html')


@app.route('/oxygen')
def oxygen():
    return render_template('oxygen.html')

@app.route('/pepper')
def pepper():
    return render_template('pepper.html')

@app.route('/plant')
def plant():
    return render_template('plant.html')

@app.route('/sandalwood')
def sandalwood():
    return render_template('sandalwood.html')

@app.route('/shatavari')
def shatavari():
    return render_template('shatavari.html')

@app.route('/skin')
def skin():
    return render_template('skin.html')

@app.route('/sub_home')
def sub_home():
    return render_template('sub_home.html')



@app.route('/tulip-ginger')
def tulip_ginger():
    return render_template('tulip-ginger.html')

@app.route('/tulsi')
def tulsi():
    return render_template('tulsi.html')

@app.route('/turmeric')
def turmeric():
    return render_template('turmeric.html')

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/hypertension')
def hypertension():
    return render_template('hypertension.html')


@app.route('/gut')
def gut():
    return render_template('gut.html')

@app.route('/hairfall')
def hairfall():
    # your code here
    return render_template('hairfall.html')




@app.route('/kideny')
def kideny():
    # your code here
    return render_template('kideny.html')

@app.route('/thyroid')
def thyroid():
    # your code here
    return render_template('thyroid.html')
 
 
@app.route('/allergy')
def allergy():
    # your code here
    return render_template('allergy.html')

@app.route('/seeds')
def seeds():
    # your code here
    return render_template('seeds.html')


# ---------------------- Auto open browser to /register ----------------------
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/register')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
