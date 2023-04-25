// let num1 = '46';
// let num2 = '4';
// let result = parseInt(num1) + parseInt(num2);
// console.log(result);

// let num1 = '46.8';
// let num2 = '4';
// let result = parseFloat(num1) + parseInt(num2);
// console.log(result);

// let num1 = 'js';
// let num2 = '22';
// let result = isNaN(num1);
// console.log(result);

// let num1 = '110';
// let num2 = parseInt(num1,2);
// console.log(num2);

let strSum = prompt("შეიყვანე ანაბრის თანხა" , 500);
let strPercent = prompt('შეიყვანეთ საპროცენტო განაკვეთი' ,5);
let sum = parseInt(strSum);
let procent = parseInt(strPercent);
sum = sum + sum * procent  / 100;
alert("პროცენტია " + sum);