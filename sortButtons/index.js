var arr=[1,2,3,4,5,6,7,8,9,10];
document.getElementById("print").innerHTML = arr;
function myFunction1()
{
    arr.sort(function(a,b){return a-b});
    document.getElementById("demo").innerHTML = arr;
}

function myFunction2()
{
    arr.sort(function(a,b){return b-a});
    document.getElementById("demo").innerHTML = arr;
}
