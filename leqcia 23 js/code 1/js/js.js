// let myArray = new Array();
// let myArray = [];
// let people = ["lia", "giorgi", "beqa"];
// document.write(people);
// document.write(people[1]);
// people[7] = "sofia";
// document.write(people[7]);

// let numbers1 = [1,2,3,4,5]; //ერთ განზომილებიანი

// let numbers2 = [[0,1,2], [3,4,5]]; //ორ განზომილებიანი
// document.write(numbers2);

// let people = [
//     ["lia", 30, false],
//     ["giorgi", 23, true],
//     ["beqa", 20, false]
// ];
// document.write(people[0][0]);

// let income = 100;
// if(income > 50){
//      let message = "შემოსავალი მეტია 50ზე";
//      alert(message);
// }

// let income = 100;
// let age = 19;
// if(income<150 && age>18){
//     let message = "";
//     alert(message);
// } 

// let age = 17;
// if(age >= 18){
//     alert("");
// } else {
//     alert("");
// }

// let income = 300;
// switch(income){
//     case 100:{
//         document.write("შემოსავალი 100ის ტოლია");
//     }break;
//     case 200:{
//         document.write("შემოსავალი 200ის ტოლია");
//     }break;
//     case 300:{
//         document.write("შემოსავალი 300ის ტოლია");
//     }break;

//     default:{
//         document.write("შემოსავალი ვერ დადგინდა");
//     }
// }

// let dayofWeek = new Date().toLocaleString("default",{weekday:"long"});


let dayofWeek = "Wednesday";
switch(dayofWeek){
    case "Monday":{
        document.write("დღეს ორშაბათია");
        break;
    }

    case "Tuesday":{
        document.write("დღეს სამშაბათი");
        break;
    }

    case "Wednesday":{
        document.write("დღეს ოთხშაბათი");
        break;
    }

    case "Thursday":{
        document.write("დღეს ხუთშაბათი");
        break;
    }

    case "Friday":{
        document.write("დღეს პარასკევი");
        break;
    }

    case "Saturday":{
        document.write("დღეს შაბათი");
        break;
    }

    case "Sunday":{
        document.write("დღეს კვირა");
        break;
    }

    default:{
        document.write("Error");
        break;
    }
}