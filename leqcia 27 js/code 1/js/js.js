// let user = new Object();

// let user = {

// }

// let user = {}
// user.name="ana";
// user.age=30;
// console.log(user.name);

// let user = {};
// user.name="ana";
// user.age=30;
// user.step = function(){
//     console.log(user.age);
// }
// user.step();
// delete user.name;
// console.log(user.name);

// let country = {
//     name:"გერმანია",
//     language:"გერმანული",
//     capital:{
//         name:"ბერლინი",
//         population:337500,
//         year:1237,
//     }
// };
// console.log("დედაქალაქი " + country.name);
// console.log("მოსახლეობა " + country["capital"]["population"]);

// let country = {
//     name:"შვეიცარია",
//     language:["გერმანული","ფრანგული","იტალიური"],
//     capital:{
//         name:"ბერნი",
//         population:1232432
//     },
//     cities:[
//         {name:"ციურიხი",population:293848237},
//         {name:"ჟენევა",population:293848237},
//         {name:"ბაზელი",population:293848237},
//     ]
// }
// document.write("<h3>" + "შვეიცარიის ოფიციალური ენებია " + "</h3>");
// for(let i = 0; i < country.language.length; i++){
//     document.write(country.language[i] + "<br>");
// }
// document.write("<h3>" + "შვეიცარიის ქალაქებია " + "</h3>");
// for(let i = 0; i < country.cities.length; i++){
//     document.write(country.cities[i].name + ": " + country.cities[i].population + "<br>");
// }


// let user = {};
// user.name="ana";
// user.age=30;
// user.step = function(){
//     console.log(user.age);
//     console.log(user.name);
// }
// let hasNameprop = "name" in user;
// console.log(hasNameprop);
// let hasNameprop = "weight" in user;
// console.log(hasNameprop);
// let hasNameprop = "ana" in user.name;
// console.log(hasNameprop);


// let user = {};
// user.name="Lasha";
// user.age=30;
// user.step = function(){
//     console.log(user.age);
//     console.log(user.name);
// };

// for(let key in user){
//     console.log(key + ":" + user[key]);
// }
