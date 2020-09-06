URL = window.URL || window.webkitURL;

var gum_stream;
var recording;
var input;

var channels = 1;
var sample_num = 0;

var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext

var start_button = document.getElementById("start");
var pause_button = document.getElementById("pause");
var stop_button = document.getElementById("end")

var sound_obj = {};

start_button.addEventListener("click",start);
pause_button.addEventListener("click",pause);
stop_button.addEventListener("click",stop);

function start(){
  console.log("initializing recording");
  var constraints = { audio: true, video:false };
  start_button.disabled = true;
  pause_button.disabled = false;
  stop_button.disabled = false;
  navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
      console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
      audioContext = new AudioContext();
      console.log("format: "+channels+" channel pcm @ "+audioContext.sampleRate/1000+"kHz");
      $.ajax({
        url:"/reinit",
        type:"POST",
        processData:false,
        data:audioContext.sampleRate
      });
      gum_stream = stream;
      input = audioContext.createMediaStreamSource(stream);
      var sound_repeat = setInterval(next, 5000);
      sound_obj.play_sound = sound_repeat;
      start_recording();
      console.log("start sample "+sample_num);


  }).catch(function(err) {
      start_button.disabled = false;
      pause_button.disabled = true;
      stop_button.disabled = true;
  });
}

function next(){
  stop_recording();
  recording.exportWAV(send_data);
  start_recording();
  playSound();
}

function playSound() {
  const audio = new Audio("https://media.geeksforgeeks.org/wp-content/uploads/20190531135120/beep.mp3");
  audio.play();
}

// function clear() {
//   sound_obj.clear = clearInterval(sound_obj.play_sound);
// }

function pause(){
  console.log("pause clicked. recording halted=",recording.recording);
  if(recording.recording){
    recording.stop();
    pause_button.innerHTML="Resume";
  }else{
    recording.record();
    pause_button.innerHTML="Pause";
  }
}

function stop(){
  console.log("stopping recording");
  start_button.disabled = false;
  stop_button.disabled = true;
  pause_button.disabled = true;
  pause_button.innerHTML = "Pause";
  sound_obj.clear = clearInterval(sound_obj.play_sound);
  stop_recording();
}

function start_recording(){
  recording = new Recorder(input,{numChannels:channels});
  recording.record();
}

function stop_recording(){
  recording.stop();
  gum_stream.getAudioTracks()[0].stop();
}

function send_data(blob) {
  var url = URL.createObjectURL(blob);
  console.log("sending data");
  $.ajax({
    url:"/postmethod",
    method:"POST",
    processData: false,
    ContentType: false,
    data:url,
    dataType:'script'
  });
}

function createDownloadLink(blob) {

	var url = URL.createObjectURL(blob);
	var au = document.createElement('audio');
	var li = document.createElement('li');
	var link = document.createElement('a');

	//name of .wav file to use during upload and download (without extendion)
	var filename = new Date().toISOString();

	//add controls to the <audio> element
	au.controls = true;
	au.src = url;

	//save to disk link
	link.href = url;
	link.download = filename+".wav"; //download forces the browser to donwload the file using the  filename
	link.innerHTML = "Save to disk";

	//add the new audio element to li
	li.appendChild(au);

	//add the filename to the li
	li.appendChild(document.createTextNode(filename+".wav "))

	//add the save to disk link to li
	li.appendChild(link);

	//upload link
	var upload = document.createElement('a');
	upload.href="#";
	upload.innerHTML = "Upload";
	upload.addEventListener("click", function(event){
		  var xhr=new XMLHttpRequest();
		  xhr.onload=function(e) {
		      if(this.readyState === 4) {
		          console.log("Server returned: ",e.target.responseText);
		      }
		  };
		  var fd=new FormData();
		  fd.append("audio_data",blob, filename);
		  xhr.open("POST","upload.php",true);
		  xhr.send(fd);
	})
	li.appendChild(document.createTextNode (" "))//add a space in between
	li.appendChild(upload)//add the upload link to li

	//add the li element to the ol
	recordingsList.appendChild(li);
}


// function startTimer(duration, display) {
//   var timer = duration, minutes, seconds;
//   setInterval(function () {
//       minutes = parseInt(timer / 60, 10);
//       seconds = parseInt(timer % 60, 10);

//       minutes = minutes < 10 ? "0" + minutes : minutes;
//       seconds = seconds < 10 ? "0" + seconds : seconds;

//       display.textContent = minutes + ":" + seconds;

//       if (--timer < 0) {
//           timer = duration;
//       }
//   }, 1000);
// }

// window.onload = function () {
//   var fiveSeconds = 5,
//       display = document.querySelector('#time');
//   startTimer(fiveSeconds, display);
// };