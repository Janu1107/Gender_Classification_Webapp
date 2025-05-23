from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('gender_classification_tutorial.sav', 'rb'))

app = Flask(_name_)



@app.route('/')
def man():
    return render_template('base.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    arr = np.array([[data1, data2, data3, data4,data5,data6,data7]])
    pred = model.predict(arr)[0]
    return render_template('after.html', data=pred)


if _name_ == "_main_":
    app.run(debug=True)
