from flask import Flask, url_for, request, json, Response, jsonify, render_template, redirect, flash
from wtforms import  SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from functools import wraps
import joblib
import numpy as np 
import pickle
import pandas as pd
import os

app = Flask(__name__)
app.config['SECRET_KEY']='mysecret'

test_data_f =  { "Age" : 10, "KM" : 25000, "HP" : 110, "CC" : 1600, "Weight" : 1200}  

class PredictForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    KM = IntegerField('KM' , validators=[DataRequired()])
    HP = IntegerField('HP' , validators=[DataRequired()])
    CC = IntegerField('CC' , validators=[DataRequired()])
    Weight = IntegerField('Weight', validators=[DataRequired()])
    submit = SubmitField('Calculate Price')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

model_pkl = pickle.load(open('CorrolaPrice.pkl','rb'))

@app.route('/hi', methods = ['GET'])
def api_hi():
    data = {
        'hello': 'hiworld',
        'number': 456
    }
    js = json.dumps(data)
    
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link']= 'http://www.cteq.eu'
    return resp

@app.route('/start',methods=['GET','POST'])
def start():
    form = PredictForm()
    if form.validate_on_submit():
        flash('Price Calculation Requested')
        test_data_f['Age']=form.age.data
        test_data_f['KM']=form.KM.data
        test_data_f['HP']=form.HP.data
        test_data_f['CC']=form.CC.data
        test_data_f['Weight']=form.Weight.data
        data = test_data_f
        result=model_pkl.predict(pd.DataFrame(pd.DataFrame(data, index=[0])))[0]      
        return render_template('result.html',title='Corolla Price Prediction', form=form, price=result)       
    return render_template('index.html', title='Corolla Price Prediction', form=form)


# This can be used with curl to test the api/webserver
@app.route('/predict', methods=['POST'])
def price_predict():
   if request.method == 'POST':
   # Get the data from the POST method
     data = request.get_json(force=True)     
   # Predict using Model loaded from pkl file 
   return jsonify(model_pkl.predict(pd.DataFrame(pd.DataFrame(data, index=[0])))[0])

@app.route('/apitest_json')
def apitest_json():
    test_data =  { "Age" : 10, "KM" : 25000, "HP" : 110, "CC" : 1600, "Weight" : 1200}    
    return jsonify(model_pkl.predict(pd.DataFrame(pd.DataFrame(test_data, index=[0])))[0])

@app.route('/apitest')
def apitest():   
    return jsonify(model_pkl.predict(pd.DataFrame([[10,25000,110,1600,1200]]))[0])

if __name__ == '__main__':
    app.run(debug=True)
   