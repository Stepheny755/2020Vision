URL = window.URL || window.webkitURL;

var gum_stream;
var recording;
var input;

var channels = 1;
var sample_num = 0;

var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext

var start_button = document.getElementById("exam_start");
var next_button = document.getElementById("exam_next");
var pause_button = document.getElementById("exam_pause");
var stop_button = document.getElementById("exam_stop")

start_button.addEventListener("click",start);
next_button.addEventListener("click",next);
pause_button.addEventListener("click",pause);
stop_button.addEventListener("click",stop);

function start(){
  console.log("initializing recording");
  var constraints = { audio: true, video:false };
  start_button.disabled = true;
  next_button.disabled = false;
  pause_button.disabled = false;
  stop_button.disabled = false;
  navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
      console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
      audioContext = new AudioContext();
      console.log("format: "+channels+" channel pcm @ "+audioContext.sampleRate/1000+"kHz");
      gum_stream = stream;
      input = audioContext.createMediaStreamSource(stream);
      recording = new Recorder(input,{numChannels:channels});
      recording.record();
      console.log("start sample "+sample_num);
  }).catch(function(err) {
      start_button.disabled = false;
      next_button.disabled = true;
      pause_button.disabled = true;
      stop_button.disabled = true;
  });
}

function next(){
  recording.stop();
  recording.exportWAV(send_data);
}

function pause(){
  console.log("pause clicked. temporarily halting recordings=",rec.recording);
  if(recording.recording){
    recording.stop();
    pause_button.innerHTML="Resume";
  }else{
    recording.record();
    pause_button.innerHTML="Pause";
  }
}

function stop(){
  console.log("stop clicked. stopping recording");
  stop_button.disabled = true;
  record_button.disabled = false;
  pause_button.disabled = false;
  pause_button.innerHTML = "Pause";
  rec.stop();
  gum_stream.getAudioTracks()[0].stop();
}

function send_data(blob) {
  var form_data = new FormData();
  form_data.append('file',blob);

  console.log("sending data");
  $.post("/postmethod",{
    js_data:blob
  });
}
function send_data(blob) {
  var form_data = new FormData();
  form_data.append('file',blob);

  console.log("sending data");
  $.ajax({
    url:"/postmethod",
    type:"POST",
    data:form_data,
    success: function(data){
      alert(data);
    }
  });
}

function startRecording() {
    console.log("recordButton clicked");

    /*
    $.post("/postmethod",{
      javascript_data: data
    })
    */
    /*
        Simple constraints object, for more advanced audio features see
        https://addpipe.com/blog/audio-constraints-getusermedia/
    */

    var constraints = { audio: true, video:false }

    /*
        Disable the record button until we get a success or fail from getUserMedia()
    */

    recordButton.disabled = true;
    stopButton.disabled = false;
    pauseButton.disabled = false

    /*
        We're using the standard promise based getUserMedia()
        https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
    */

    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
        console.log("getUserMedia() success, stream created, initializing Recorder.js ...");

        /*
            create an audio context after getUserMedia is called
            sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
            the sampleRate defaults to the one set in your OS for your playback device

        */
        audioContext = new AudioContext();

        //update the format
        document.getElementById("formats").innerHTML="Format: 1 channel pcm @ "+audioContext.sampleRate/1000+"kHz"

        /*  assign to gum_stream for later use  */
        gum_stream = stream;

        /* use the stream */
        input = audioContext.createMediaStreamSource(stream);

        /*
            Create the Recorder object and configure to record mono sound (1 channel)
            Recording 2 channels  will double the file size
        */
        rec = new Recorder(input,{numChannels:1})

        //start the recording process
        rec.record()

        console.log("Recording started");

    }).catch(function(err) {
        //enable the record button if getUserMedia() fails
        recordButton.disabled = false;
        stopButton.disabled = true;
        pauseButton.disabled = true
    });
}

function sendData(blob){
  var formData = new FormData();
  formData.append('file',blob,'filename');

  $.post({
      type: 'POST',
      url: 'ServerURL',
      data: form, // Our pretty new form
      cache: false,
      processData: false, // tell jQuery not to process the data
      contentType: false // tell jQuery not to set contentType
      }).done(function(data) {
        console.log(data);
    });
}

function pauseRecording(){
    console.log("pauseButton clicked rec.recording=",rec.recording );
    if (rec.recording){
        //pause
        rec.stop();
        pauseButton.innerHTML="Resume";
    }else{
        //resume
        rec.record()
        pauseButton.innerHTML="Pause";

    }
}

function stopRecording() {
    console.log("stopButton clicked");

    //disable the stop button, enable the record too allow for new recordings
    stopButton.disabled = true;
    recordButton.disabled = false;
    pauseButton.disabled = true;

    //reset button just in case the recording is stopped while paused
    pauseButton.innerHTML="Pause";

    //tell the recorder to stop the recording
    rec.stop();

    //stop microphone access
    gum_stream.getAudioTracks()[0].stop();

    //create the wav blob and pass it on to
    rec.exportWAV(sendData);
}
