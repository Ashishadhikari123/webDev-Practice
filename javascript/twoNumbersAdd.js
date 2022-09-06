function addTwoNumbers(a,b){
    return a+b;
}

var a = prompt("Enter first number");
var b = prompt("Enter second number");
//parseInt() is  used to convert string to parseInt
var c = addTwoNumbers(parseInt(a),parseInt(b));
alert("Sum of 2 numbers is " + c);

