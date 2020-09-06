// startButton would let the app know when to start recording/listening
var startButton = document.querySelector("#start"); 
// endButton would let the app know when to stop recording/listening
var endButton = document.querySelector("#end");
var scoreButton = document.querySelector("#getScore");
var resetButton = document.querySelector("#reset");

var scoreDisplay = document.querySelector("#scoreDisplay");
var score = 0;

scoreButton.addEventListener("click", function(){
    score = 1; // would change this to whatever the actual score turns out to be based on back-end integration
    scoreDisplay.textContent = score;
})

resetButton.addEventListener("click", function(){
	reset();
})

function reset() {
    score = 0;
    scoreDisplay.textContent = score;
}