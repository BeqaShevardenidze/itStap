// function br(){
//     document.write("<br>");
// }

// let arr = [], size = 10;
// for(let i = 0; i < size; i++){
//     arr[i] = Math.floor(Math.random()*10);
// }


// for(let i = 0; i < size; i++){
//     document.write(arr[i] + " ");
// }

// br(); br();

// // let num = prompt("ჩაწერეთ რიცხვი");
// for(let i = 0; i < size; i++){
//     if (arr[i] === parseInt(num)){
//         document.write("უდრუს"); br();
//     }else {
//         document.write(arr[i]); br();
//     }
// }

// function Mfunk(){
//     let str = document.getElementById("inputText");
//     let strVal = str.ariaValueMax;
//     alert(strVal);
// }

// let button = document.getElementById("send");
// button.addEventListener("click",Mfunk);



// let numbRand = 5;
let numbRand = Math.floor(Math.random()*11);
let sicocxle = 3;

do{
    let number = prompt("ჩაწერეთ ციფრი ერთოდან ათის ჩათვლით");
    if(number == numbRand){
        alert("თქვენ გამოიცანით ციფრი,  გილოცავთ");
        break;
    } else if(sicocxle == 0){
        alert("Game Over");
    } else {
        sicocxle = sicocxle-1;
        alert("თქვენ ვერ გამოიცანით: დარჩენილი სიცოცხლეა! " + sicocxle);
    }
}while(sicocxle > 0);