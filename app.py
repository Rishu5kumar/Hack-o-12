from flask import Flask,request,render_template,redirect,url_for
import numpy as np
import pandas as pd
import sklearn
import pickle
import os
import json
# from PIL import Image

# import tensorflow as tf
# import streamlit as st


# working_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = f"{working_dir}/trained_model/plant_disease_prediction_model.h5"
# # Load the pre-trained model
# model = tf.keras.models.load_model(model_path)

# # loading the class names
# class_indices = json.load(open(f"{working_dir}/class_indices.json"))


# # Function to Load and Preprocess the Image using Pillow
# def load_and_preprocess_image(image_path, target_size=(224, 224)):
#     # Load the image
#     img = Image.open(image_path)
#     # Resize the image
#     img = img.resize(target_size)
#     # Convert the image to a numpy array
#     img_array = np.array(img)
#     # Add batch dimension
#     img_array = np.expand_dims(img_array, axis=0)
#     # Scale the image values to [0, 1]
#     img_array = img_array.astype('float32') / 255.
#     return img_array


# # Function to Predict the Class of an Image
# def predict_image_class(model, image_path, class_indices):
#     preprocessed_img = load_and_preprocess_image(image_path)
#     predictions = model.predict(preprocessed_img)
#     predicted_class_index = np.argmax(predictions, axis=1)[0]
#     predicted_class_name = class_indices[str(predicted_class_index)]
#     return predicted_class_name


# # Streamlit App
# st.title('Plant Disease Classifier')

# uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

# if uploaded_image is not None:
#     image = Image.open(uploaded_image)
#     col1, col2 = st.columns(2)

#     with col1:
#         resized_img = image.resize((150, 150))
#         st.image(resized_img)

#     with col2:
#         if st.button('Classify'):
#             # Preprocess the uploaded image and predict the class
#             prediction = predict_image_class(model, uploaded_image, class_indices)
#             st.success(f'Prediction: {str(prediction)}')
            
            
# importing model
model = pickle.load(open('models/model.pkl','rb'))
sc = pickle.load(open('models/standscaler.pkl','rb'))
ms = pickle.load(open('models/minmaxscaler.pkl','rb'))
dtr = pickle.load(open('models/dtr.pkl','rb'))
preprocessor = pickle.load(open('models/preprocessor.pkl','rb'))


app = Flask(__name__)


users = [
    {'name':'user1', 'email': 'user1@example.com', 'password': 'password1'},
    {'name':'user2', 'email': 'user2@example.com', 'password': 'password2'}
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

@app.route('/logout')
def logout():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
