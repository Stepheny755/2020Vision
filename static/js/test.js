
var testButton = document.getElementById("testButton");
testButton.addEventListener("click",getData);

function getData() {
  console.log("button clicked");
  var outputData = "test";
  $.post("/postmethod",{
    js_data:JSON.stringify(outputData)
  });
}
