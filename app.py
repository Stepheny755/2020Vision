#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route("/postmethod",methods=['POST'])
def get_js_data_post():
    jsdata = request.form['javascript_data']
    print(jsdata)
    #with open("file.wav","wb") as f:
        #f.write(request.data)
    print("msg written")
    return

if __name__ == "__main__":
    app.run(debug=True)
