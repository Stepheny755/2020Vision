#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request, render_template, make_response
import os, pickle

app = Flask(__name__)
app.debug = True

class track():
    def __init__(self,audio_path):
        self.value = 0
        self.audio_path = audio_path
        self.ext = ".mp3"
        self.create_path_with_check()

    def create_path_with_check(self):
        if not os.path.exists(self.audio_path):
            os.makedirs(self.audio_path)
        pass

    def clear_audio_dir(self):
        for f in [ f for f in os.listdir(self.audio_path) if f.endswith(self.ext) ]:
            os.remove(os.path.join(self.audio_path, f))
        pass

    def save_audio(self,data,name):
        complete_path = os.path.join(self.audio_path,name)+self.ext
        with open(complete_path,"wb") as f:
            f.write(data)
        pass

    def increment_value(self):
        self.value = self.value + 1
        return self.value

    def get_value(self):
        return self.value

t = track("audio")

#landing
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('layouts/index.html')

@app.route("/reinit",methods=['POST'])
def init():
    t = track("audio")
    return


@app.route("/postmethod",methods=['POST'])
def post_js_data():
    jsdata = request.form
    t.increment_value()
    with open("file.wav","wb") as f:
        f.write(request.data)
    print("msg received")
    return "1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
