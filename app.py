from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras import *
import numpy as np

physical_devices = tf.config.list_physical_devices('GPU') 
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)

app = Flask(__name__)

def init():
    global md
    md = models.load_model('diabets.h5')
    print("Model loaded!")


def preprocess(arr):
    data = np.array(arr)
    data = np.reshape(data, (-1, 8))
    return data


@app.route('/')
def survey():
    return render_template('main.html')

@app.route('/survey')
def main():
    return render_template('survey.html')

@app.route('/law')
def law():
    return render_template('law.html')

@app.route('/result')
def reulst():
    return render_template('result.html')


@app.route('/submit', methods=['POST'])
def output():
    print('Get Value')
    try:
        a = float(request.form['Pregnancies'])
        b = float(request.form['Glucose'])
        c = float(request.form['BloodPressure'])
        d = float(request.form['SkinThickness'])
        e = float(request.form['Insulin'])
        f = float(request.form['BMI'])
        g = float(request.form['DiabetesPedigreeFunction'])
        h = float(request.form['Age'])
    except:
        return render_template('404.html')

    print('Preprocessing')
    Xdata = [a, b, c, d, e, f, g, h]
    Xdata = preprocess(Xdata)

    print('Predict')
    res = md.predict(Xdata).tolist()
    out = {'not_diabetes':res[0][0], 'diabetes':res[0][1]}
    return render_template('result.html', out=out, Xdata=Xdata[0])



if __name__ == "__main__":
    init()
    app.run('0.0.0.0', port=80, debug=True)


