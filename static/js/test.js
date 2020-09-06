
var testButton = document.getElementById("testButton");
testButton.addEventListener("click",getData);

function getData() {
  console.log("button clicked");
  var outputData = "test";
  $.ajax({
    url: "/postmethod",
    type: "POST",
    data:JSON.stringify(outputData)
  });
}
