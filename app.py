#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request, render_template, make_response
import os, pickle, json, struct
from api.middleware import upload_file

app = Flask(__name__)
app.debug = True

class track():
    def __init__(self,audio_path,sample_rate):
        self.value = 0
        self.sr = sample_rate
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

default_sr = 48000
t = track("audio",default_sr)

#landing
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('layouts/index.html')

#re-init exam
@app.route("/reinit",methods=['POST'])
def init():
    jsdata = request.form.to_dict()
    target_sr = int(list(jsdata.keys())[0])
    t = track("audio",target_sr)
    print("starting new exam with sample rate "+str(target_sr))
    return jsonify(t.get_value())

#favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

#audio data
@app.route("/postmethod",methods=['POST'])
def post_js_data():
    jsdata = request.form.to_dict()
    format_url = list(jsdata.keys())[0].replace("blob:","")
    upload_file(format_url,t.get_value())
    t.increment_value()
    return jsonify(t.get_value())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
