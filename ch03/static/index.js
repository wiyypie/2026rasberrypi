let count = 0;

const number = document.getElementById("number");
const increaseButton = document.getElementById("increase");
const sendButton = document.getElementById("send");

increaseButton.addEventListener("click", function () {
    count++;
    number.innerText = count;
});

sendButton.addEventListener("click", function () {
    location.href='http://라즈베리파이주소:5000/'+count
    count = 0;
    number.innerText = count;
});
