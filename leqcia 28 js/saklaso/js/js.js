function br(){
    document.write("<br>");
}

let x;
x = prompt("აირჩიეთ ვარიანტი N1 N2");
switch(parseInt(x)){
    case 1:{
        let arr = ["მანქანა", 69, 102, "ტესტი", 404, "მასივი"];

        document.write("საწყისი მასივი: "); br();
        for(let i=0; i<arr.length; i++){
            document.write(arr[i] + ", ");
        }
        
        document.write("მასივში არსებული ციფრები: "); br();
        for(let i=0; i<arr.length; i++){
            if(arr[i] <= 99999999){
                document.write(parseInt(arr[i]) + ", ");
            }
        }
        break;
    }

    case 2:{
        let randSimbol = ["რძე", 77, 11, "თაფლი", -88];
        function arryTest(anyArray){
            for(let i=0; i<anyArray.length; i++){
                if(isNaN(anyArray[i])){
                    document.write("მასივში არსებული ელემენტი: " + arryTest[i] + " არ შეიცევა ციფრს ან ციფრებს"); br();
                }else{
                    document.write("მასივში არსებული ელემენტი: " + anyArray + "შეიცავს ციფრებს ან ელემენტებს"); br();
                }
            }
        }
        arryTest(randSimbol);
        break;
    }

    default:{
        alert("error");
        break;
    }
}