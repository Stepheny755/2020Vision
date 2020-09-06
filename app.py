#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request, render_template, make_response
import os, pickle, json

app = Flask(__name__)
app.debug = True

class track():
    def __init__(self,audio_path):
        self.value = 0
        self.audio_path = audio_path
        self.ext = ".wav"
        self.create_path_with_check()
        self.clear_audio_dir()

    def create_path_with_check(self):
        if not os.path.exists(self.audio_path):
            os.makedirs(self.audio_path)
        pass

    def clear_audio_dir(self):
        for f in [ f for f in os.listdir(self.audio_path) if f.endswith(self.ext) ]:
            os.remove(os.path.join(self.audio_path, f))
        pass

    def save_audio_name(self,data,name):
        complete_path = os.path.join(self.audio_path,name)+self.ext
        with open(complete_path,"wb") as f:
            f.write(data)
        pass

    def save_audio(self,data):
        self.save_audio_name(data,str(self.value))

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

#re-init exam
@app.route("/reinit",methods=['POST'])
def init():
    t = track("audio")
    print("starting new exam...")
    return jsonify(t.get_value())

#audio data
@app.route("/postmethod",methods=['POST'])
def post_js_data():
    jsdata = request.form.to_dict()
    print(jsdata)
    t.save_audio(json.dumps(jsdata))#.encode('utf-8'))
    t.increment_value()
    print("msg received")
    return "1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
