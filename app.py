from flask import Flask,request,render_template,redirect,url_for
import numpy as np
import pandas as pd
import sklearn
import pickle
import os
import json

# importing model
model = pickle.load(open('models/model.pkl','rb'))
sc = pickle.load(open('models/standscaler.pkl','rb'))
ms = pickle.load(open('models/minmaxscaler.pkl','rb'))
dtr = pickle.load(open('models/dtr.pkl','rb'))
preprocessor = pickle.load(open('models/preprocessor.pkl','rb'))
fermodel = pickle.load(open('models/fert_model.pkl','rb'))


app = Flask(__name__)


users = [
    {'name':'user1', 'email': 'user1@example.com', 'password': 'password1'},
    {'name':'user2', 'email': 'user2@example.com', 'password': 'password2'},
    {'name':'Rounak', 'email': 'rounakbiswal2003@gmail.com', 'password': 'rounak'},
    {'name':'rishu', 'email': 'kumar05.rishu@gmai.com', 'password': 'rishu'},
    {'name':'niharika', 'email': 'nbniharika24@gmail.com', 'password': 'niharika'},
    {'name':'yashmin', 'email': 'swain74yasmin@gmail.com', 'password': 'yasmin'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginfarm', methods=['POST'])
def loginfarm():
    email = request.form.get('email')
    password = request.form.get('password')
    for user in users:
        if user['email'] == email and user['password'] == password:
            return redirect(url_for('hero'))    
    return redirect(url_for('index'))

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    for user in users:
        if user['email'] == email:
            # Email already exists, redirect back to signup page
            return redirect(url_for('index'))
    
    # Add the new user to the database
    users.append({'name':name, 'email': email, 'password': password})
    return redirect(url_for('index'))

@app.route('/hero')
def hero():
    return render_template('hero.html')

@app.route('/consultancy')
def consultancy():
    return render_template('consultancy.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

@app.route('/loan')
def loan():
    return render_template('loan.html')

@app.route('/buyerseller')
def buyerseller():
    return render_template('buyerseller.html')

@app.route('/budget')
def budget():
    return render_template('budgetindex.html')

@app.route('/govt')
def govt():
    return render_template('govt.html')

@app.route('/seed')
def seed():
    return render_template('seed.html')
@app.route('/solarpanel')
def solarpanel():
    return render_template('solarpanel.html')
@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/predictfarm')
def predictfarm():
    return render_template("predict.html")

@app.route('/water')
def water():
    return render_template("water.html")


@app.route("/predict",methods=['POST'])
def predict():
    N = request.form['Nitrogen']
    P = request.form['Phosporus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['Ph']
    rainfall = request.form['Rainfall']

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return render_template('predict.html',result = result)



@app.route('/yieldpredict')
def yieldpredict():
    return render_template("yield.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback_form.html")
@app.route("/yields",methods=['POST'])
def yields():
    if request.method == 'POST':
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        Area = request.form['Area']
        Item  = request.form['Item']

        features = np.array([[Year,average_rain_fall_mm_per_year,pesticides_tonnes,avg_temp,Area,Item]],dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = int(dtr.predict(transformed_features).reshape(1,-1)[0])

        return render_template('yield.html',prediction = prediction)

@app.route('/predictfer')
def predictfer():
    return render_template("ferpredict.html")

@app.route('/wea')
def wea():
    return render_template("wea.html")

@app.route('/ferpred', methods=['POST'])
def ferpred():
    if request.method == 'POST':
        # Get the input values from the form
        Temperature = request.form['Temperature']
        Humidity = request.form['Humidity']
        Moisture = request.form['Moisture']
        # Soil_Type = request.form['Soil_Type']
        # Crop_Type = request.form['Crop_Type']
        Nitrogen = request.form['Nitrogen']
        Potassium = request.form['Potassium']
        Phosphorous = request.form['Phosphorous']

        # Make prediction
        pred = model.predict([[Temperature, Humidity, Moisture, 40, Nitrogen, Potassium, Phosphorous,]])[0]

        # Render the prediction result template with the prediction
        return render_template('ferpredict.html', result=pred)

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contactus_form.html')
if __name__ == "__main__":
    app.run(debug=True)
