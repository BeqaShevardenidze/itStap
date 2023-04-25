// let students = ["sudenti1","sudenti2","sudenti3","sudenti4"];
// for(let i = 0; i < students.length; i++){
//     document.write(students[i]+"</br>");
// }

// let students = ["sudenti1","sudenti2","sudenti3","sudenti4"];
// for(let i = students.length -1; i >= 0; i--){
//     document.write(students[i]+"</br>");
// }

// let students = ["sudenti1","sudenti2","sudenti3","sudenti4"];
// for(let index in students){
//     document.write(students[index]+"</br>");
// }


// let students = ["sudenti1","sudenti2","sudenti3","sudenti4"];
// index = 0;
// while(index < students.length){
//     document.write(students[index]+"</br>");
//     index++;
// }


// let x = 1;
// do{
//     document.write(x*x+"</br>");
//     x++;
// }while(x<10);

// let arr = [1, 2, 3, 4, 5, 12, 17, 6, 7];
// for(let i = 0; i<arr.length; i++){
//     if(arr[i]>10)

//     break;
//     document.write(arr[i]+"</br>");
// }

// let arr = [1, 2, 3, 4, 5, 12, 17, 6, 7];
// for(let i = 0; i<arr.length; i++){
//     if(arr[i]>10)
//     continue;
//     document.write(arr[i]+"</br>");
// }





let arr = [];
let x;
for(let i = 0; i < 10; i++){
    x = Math.floor(Math.random() * 17 );
    arr[i]=x;
    document.write(arr[i] + "<br>");
}