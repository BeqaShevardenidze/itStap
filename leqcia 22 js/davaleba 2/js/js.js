// var number = prompt('ჩაწერეთ ნებისმიერი რიცხვი');
// var result = parseInt(number);
// if(result % 2 == 0){
// alert('თქვენი ჩაწერილი რიცხვი ლუწია');
// }
// else{
//     alert('თქვენი ჩაწერილი რიცხვი კენტია');
// }

var strNum1 = prompt('ჩაწერეთ პირველი რიცხვი');
var strNum2 = prompt('ჩაწერეთ მეორე რიცხვი');
var strNum3 = prompt('ჩაწერეთ მესამე რიცხვი');
alert('ფორმულა: (num1 + num2) / num3');
var result = (parseInt(strNum1) + parseInt(strNum2)) / parseInt(strNum3);
alert('პასუხი = ' + result);