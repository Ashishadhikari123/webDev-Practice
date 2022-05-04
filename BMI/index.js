var weight = prompt("Enter your weight in kg ");
var height = prompt("Enter your height in m ");

function calculateBMI(weight,height){
    return (weight/(height*height));
}

document.write("Your BMI value is "+ calculateBMI(Number(weight),Number(height)));
