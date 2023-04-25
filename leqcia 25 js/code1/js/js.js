// var arr = [], size = 1000;
// for(var i = 0; i < size; i++)
// {
//     var x = Math.floor(Math.random()*100);
//     arr[i]=x;
// }
// for(var i = 0; i < size; i++)
// {
//     if(i == 50)
//     {
//         document.write(arr[i] + ", " + "</br>");
//     }
//     else
//     {
//         document.write(arr[i] + ", ");
//     }
// }

// =============================== \\

// function step(){
//     document.write("text");
// }
// step();

// function goodMorning(){
//     document.write("დილა მშვიდობისა");
// }
// function goodEvening(){
//     document.write("საღამო მშვიდობისა");
// }
// let message = goodMorning;
// message();
// message = goodEvening;
// message();

// let step = function (){
//     document.write("text");
// }
// step();

// function step(x){
//     let z = x*x;
//     document.write(x + " კვადრატში ტოლია " + z);
// }
// step(50);

// function step(x,func){
//     let message = func(x);
//     document.write(message);
// }
// function wellcomeMessage(time){
//     if(time<12){
//         return"დილამშვიდობისა!";
//     }else{
//         return"დღე მშვიდობისა!";
//     }
// }
// step(13,wellcomeMessage);

// let x = 5;
// function step(){
//     let z = x*x;
//     console.log(z);
//     alert(z);
//     document.write(z);
// }

// let z = 89;
// function step(){
//     let z = 10;
//     console.log(z);
//     alert(z);
// }
// step();
// {
//     let z = 11;
//     alert(z);
// }
// alert(z);

// function step(){
//     console.log("დილამშვიდობისა! ");
//     document.write("დილამშვიდობისა! ");
//     step=function(){
//         console.log("დღე მშვიდობისა! ");
//         document.write("დღე მშვიდობისა! ");
//     }
// }
// step();
// step();
// let stepMessage=step;
// stepMessage();
// stepMessage();

let text = ["გიორგიმ გუშინ დაკარგა საკუთარი საკრედიტო ბარათი, რომლის ნომერია 1178-9087-2384-8787, გიორგი დაუყოვნებლივ წავიდა ბანკში და დააფიქსირა არსებული შემთხვევა, რის გამოც მას მისცეს ახალი საკრედიტო ბარათი ნომრით: 1103-8899-0811-1722."];
document.write(text.splite(''));
for(let i=0; i < text.length; i++){
    for(let j = 0; j < text[i].length; j++){
        document.write(text[j]);

        for(let k=0; k<text.length; i++){
            if(parseInt(text[j])==k){
                // console.log(text[j]);
            }
        }
    }
}