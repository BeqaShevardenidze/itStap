function br(){
    document.write("<br>");
}

var x;
x = prompt("აირჩიეთ ამოცანა: " + " N1 " + " N2 ");
switch(parseInt(x)){
    case 1:{
        document.write("დავალება N1: <br> გააკეთეთ თქვენი ჯგუფის შესახებ ობიექტი , სადაც იქნება მცირედი ინფორმაცია მოცემული.");

        var myStat = [
            {subject: "მათემატიკა", score: (9)},
            {subject: "ფიზიკა", score: (10)},
            {subject: "ბიოლოგია", score: (8)}
        ];
        console.log(myStat);
        break;
    }

    case 2:{
        var x2;
        x2 = prompt("ამოცანის ამოხსნის ორი ვარიანტი არსებობს. აირჩიეთ: N1 N2");

        switch(parseInt(x2)){
            case 1:{
                let drinks = [
                    ["cola", 25],
                    ["pepsi", 20],
                    ["fanta", 30]
                ];
                document.write("საწყისი მასივი: " + drinks); br();

                let result = [];
                for(let i = 0; i < drinks.length; i++){
                    result[i] = drinks[i][1];
                }
                document.write("ფასების მასივი: " + result); br();

                let temp;
                for(let i = 0; i<result.length; i++){
                    for(let j = 0; j < result.length + 1; j++){
                        if(result[i] < result[j]){
                            temp = result[i];
                            result[i] = result[j];
                            result[j] = temp;
                        }
                    }
                }
                document.write("ფასები ზრდადობის მიხედვით: " + result); br();
                break;
            }
            case 2:{
                let drinks = [
                    { name: "Coffee", price: 2.5 },
                    { name: "Tea", price: 1.5 },
                    { name: "Juice", price: 3.5 }
                  ];
                  const sortedDrinks = drinks.sort((a, b) => a.price - b.price);
                  console.log(sortedDrinks);
                break;
            }
            default:{
                alert("error");
                break;
            }
        }
        break;
    }
    default:{ 
        alert("error");
        break;
}
}