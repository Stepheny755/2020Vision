#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request, render_template, make_response
import os

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('layouts/base.html')

#@app.route()

@app.route("/postmethod",methods=['POST'])
def post_js_data():
    jsdata = request.form['js_data']
    print(jsdata)
    #with open("file.wav","wb") as f:
        #f.write(request.data)
    print("msg written")
    return "1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
