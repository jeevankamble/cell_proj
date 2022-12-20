from flask import Flask ,jsonify ,request,render_template, redirect, url_for
import config1
import numpy as np
from utils import CellPhonePrice

app = Flask(__name__)

@app.route('/')
def hello_flask():

    return render_template("index.html")

@app.route('/predicted',methods = ['GET','POST'])
def prediction():
    if request.method  == 'POST':
        data = request.form
        print('data : ',data)

        phone_price = CellPhonePrice(data)
        price = phone_price.get_predicted_price()
        print ('*******',price)
        return render_template("index.html", prediction= price)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)