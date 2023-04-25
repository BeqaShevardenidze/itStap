// function test(){
//     document.write("test function" + "<br>");
// }
// test();

// function test2(x){
//     document.write(x + x); 
// }
// var m = Math.floor(Math.random() * 10);
// test2(m);

// let arr = [10, 11, 5, 3];
// let x;

// for(let i = 0; i < arr.length; i++){
//     if(arr(1) > arr(i + 1)){
//         arr(i = x);
//     }
// }

// const arr = ['1456G', '1KG', '.5T', '.005T', '78645G', '23KG'];
// const arrangeWeights = (arr = []) => {
//    const sorted=(w)=>{
//       if(w.slice(-2) === 'KG'){
//          return +w.slice(0,-2) * 1;
//       }else if(w.slice(-1)==='T'){
//          return +w.slice(0, -1)*1000
//       }else{
//          return +w.slice(0, -1)*0.001;
//       };
//    };
//    return arr.sort((a, b) => sorted(a) - sorted(b));
// };
// document.write(arrangeWeights(arr));




// N1

// let stepGroup = [{name:"ბექა", age:"26"}, 
// {name: "სალომე", age: "25"}, 
// {name:"გიგი", age: "20" }];
// console.log(stepGroup);

// let stepGroup = ["ბექა", "სალომე", "გიგი"];
// document.write(stepGroup);



////////////////////////////////////////////
// N2



// let drinks = [
//     {name: "cola", price: 25},
//     {name: "pepsi", price: 20},
//     {name: "fanta", price: 30}
// ];
// function func(x){
//     console.log(x);
// }
// func(drinks);

// document.getElementById("demo").innerHTML =
// drinks.name + " is " + drinks.age + " years old.";

// document.write(drinks.name);



// let arr = [];
// let arr2 = [
//     [1, 2],
//     [4, 5]
// ];
// for(let i = 0; i<drinks.length; i++){
//         arr[i] = arr2[i][0];
// }
// console.log(arr);



// let arr = [5,1,3,7,10,30,0];
// let temp;
// for(let i = 0; i < arr.length; i++){

//     for(j = i + 1; j < arr.length; j++){

//         if(arr[j] < arr[i]){
//             temp = arr[i];
//             arr[i] = arr[j];
//             arr[j] = temp;
//         }
//     }
// }
// document.write(arr);


// let drinks = [
//     ["cola", 25],
//     ["pepsi", 20],
//     ["fanta", 30]
// ];
// let result = [];

// for(let i = 0; i<drinks.length; i++){
//     result[i] = drinks[i][1];
// }
// document.write("ფასების მასივი: " + result + "<br>");

// let temp;
// for(i = 0; i < result.length; i++){
//     for(let j = 0; j < result.length + 1; j++){
//         if (result[i] < result[j]){
//             temp = result[i];
//             result[i] = result[j];
//             result[j] = temp;
//         }
//     }
// }

// document.write("ფასების ზრდადობის მიხედვით: " + result + "<br>");

let arr = ["test", "beka",];
let arr2 = [];
let br = "<br>";
for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr.length; j++){
        arr2[i][j] = arr[i].charAt(0)[j].charAt(0);
    }
}
document.write(arr2 + br);




// let test = "test";
// let newArr = [];
// for(let i = 0; i < test.length; i++){
//     newArr[i] = test[i].charAt(0); 
//     document.write(newArr[i]);
// }

// document.write(br + newArr[2])







