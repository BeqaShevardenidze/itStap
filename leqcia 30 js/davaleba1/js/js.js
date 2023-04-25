let form = document.getElementById("form");

let sicocxle;

function funqcia(event){
    
    event.preventDefault();

    let numb = form.querySelector('[name="numb"]');

    let intNumb = {
        numb: numb.value,
    }

    let MyNumber = intNumb.numb;
    // let randNumb = Math.floor(Math.random()*11);
    let randNumb = 1;
    sicocxle = 3;
    

    function f1(){
        if(randNumb == MyNumber){
            document.getElementById("sicocxle").innerHTML = "დარჩენილი სიცოცხლეა: " + sicocxle;
            document.getElementById("pasuxi").innerHTML = "თქვენ მოიგეთ";
        } else if(randNumb != MyNumber) {
            sicocxle--;
            document.getElementById("sicocxle").innerHTML = "დარჩენილი სიცოცხლეა: " + sicocxle;
            document.getElementById("pasuxi").innerHTML = "ვერ გამოიცანით";
            document.getElementById("chemicifri").innerHTML = "თქვენი ჩაწერილი რიცხვია " + MyNumber;
        }
    }
    f1();
}

form.addEventListener("submit",funqcia);
