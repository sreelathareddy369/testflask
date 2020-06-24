# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:56:53 2020

@author: sreebhaskar
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome all"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is"+str(prediction)



@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier(df_test)
    return "The predicted value for the csv"+str(list(prediction))



if __name__=='__main__':
    app.run()
