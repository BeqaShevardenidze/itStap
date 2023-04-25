// "I5", "I3", "Pentium", "Seleron", "Atom"

// let personalComputer = {
//     cpu: ["I5", "I3", "Pentium", "Seleron", "Atom"],
// }

// document.write("<h3>" + "კომპიტერის პროცესორებია: " + "</h3>");
// for(let i = 0; i < personalComputer.cpu.length; i++){
//     document.write(personalComputer.cpu[i] + "<br>");
// }


function br(){
    document.write("<br>");
}
function hr(){
    document.write("<hr>");
}
let h3 = "<h3>", h3end = "</h3>";

let personalComputer = {
    cpu: {
        I7:{
            model:["1360P","1370P","1370PE"],
        }, 
        I5:{
            model:["6300U","6360U","7440HQ"],
        },
        },

    ram:{
        DDR3:{
            standart:["DDR3-800", "DDR3-1066", "DDR3-1333", "DDR3-1600"],
        },
        DDR4:{
            standart:["DDR4-1600L", "DDR4-1866N", "DDR4-2133R", "DDR4-2400U"],
        }
    },
}
document.write(h3 + "I7-ის პროცესორის მოდელებია: " + h3end); hr();
for(let i = 0; i < personalComputer.cpu.I7.model.length; i++){
    document.write(personalComputer.cpu.I7.model[i]); br();
} br(); br();

document.write(h3 + "I5-ის პროცესორის მოდელებია: " + h3end); hr();
for(let i = 0; i < personalComputer.cpu.I5.model.length; i++){
    document.write(personalComputer.cpu.I5.model[i]); br();
} br(); br();

document.write(h3 + "DDR3 -ის ოპერატიული მეხსიერების სერიებია: " + h3end); hr();
for(let i = 0; i < personalComputer.ram.DDR3.standart.length; i++){
    document.write(personalComputer.ram.DDR3.standart[i]); br();
} br(); br();

document.write(h3 + "DDR4 -ის ოპერატიული მეხსიერების სერიებია: " + h3end); hr();
for(let i = 0; i < personalComputer.ram.DDR4.standart.length; i++){
    document.write(personalComputer.ram.DDR4.standart[i]); br();
} br(); br();



// let arr = [];
// for(let i = 0; i < personalComputer.length; i++){
//     arr[i] = personalComputer;
// }
// for(let i = 0; i < personalComputer.length; i++){
//     document.write(arr[i]); br();
// }

console.log(personalComputer); br();