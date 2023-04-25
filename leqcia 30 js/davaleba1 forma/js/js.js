let form = document.getElementById("form");

let sicocxle = 10;

function funqcia(event){
    
    event.preventDefault();

    let numb = form.querySelector('[name="numb"]');

    let intNumb = {
        numb: numb.value,
    }

    let MyNumber = intNumb.numb;
    let randNumb = Math.floor(Math.random()*11);

        if(randNumb == MyNumber){
            document.getElementById("sicocxle").innerHTML = "დარჩენილი სიცოცხლეა: " + sicocxle;
            document.getElementById("pasuxi").style.color = "green";
            document.getElementById("pasuxi").innerHTML = "თქვენ მოიგეთ";
            alert("თქვენ მოიგეთ");
        } else if(sicocxle == 0){
            alert("თქვენ წააგეთ");
        } else {
            sicocxle = sicocxle-1;
            document.getElementById("sicocxle").innerHTML = "დარჩენილი სიცოცხლეა: " + sicocxle;
            document.getElementById("pasuxi").style.color = "red";
            document.getElementById("pasuxi").innerHTML = "ვერ გამოიცანით";
            document.getElementById("chemicifri").innerHTML = "თქვენი ჩაწერილი რიცხვია " + MyNumber;
        }
}

form.addEventListener("submit",funqcia);
