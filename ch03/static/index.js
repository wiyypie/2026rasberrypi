let count = 0;

const number = document.getElementById("number");
const increaseButton = document.getElementById("increase");
const sendButton = document.getElementById("send");

increaseButton.addEventListener("click", function () {
    count++;
    number.innerText = count;
});

sendButton.addEventListener("click", function () {
    location.href='http://10.150.1.0:5001/'+count
    count = 0;
    number.innerText = count;
});
