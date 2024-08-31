let textBox = document.getElementById("textBox") // input number 
let toFahrenheit = document.getElementById("toFahrenheit") // input number 
let toCelsius = document.getElementById("toCelsius") // input number 
let result = document.getElementById("result") // input number 
let temp;

function cover(){

    if(toFahrenheit.checked){
        temp = Number(textBox.value)
        temp = (temp*9)/5+32
        result.textContent= temp.toFixed(1) +'F°'
    } else if(toCelsius.checked){
        temp = Number(textBox.value)
        temp = (temp -32)*5/9
        result.textContent= temp.toFixed(1) +'C°';
    }else{
        result.textContent='Select unit';
    }
}