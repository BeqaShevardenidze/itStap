// function User(pName,pAge){
//     this.name=pName;
//     this.Page=pAge;
//     this.stepInfo=function(){
//         document.write("სახელი",this.name+"ასაკი"+"<br>")
//     };
// };
// User.prototype.hello=function(){
//     document.write(this.name+"ამბობს'გამარჯობა'!<br>");
// }
// User.prototype.maxAge=110;
// let lia=new User("ლია",30);
// lia.hello();
// let lado=new User("ლადო",24);
// lado.hello();
// console.log(lia.maxAge);
// console.log(lado.maxAge);


// function User(pName,pAge){
//     this.name=pName;
//     this.Page=pAge;
//     this.stepInfo=function(){
//         document.write("სახელი",this.name+"ასაკი"+"<br>");
//     };
// };

// User.prototype.hello=function(){
//     document.write(this.name+"ამბობს'გამარჯობა'!<br>");
// };

// User.prototype.maxAge=110;
// let lia=new User("ლია",30);
// lia.hello();
// let lado=new User("ლადო",24);
// lia.maxAge=99;
// lado.hello();
// console.log(lia.maxAge);
// console.log(lado.maxAge);


// //////////////////////////////////////////////////




//////////მოვლენები///////////////


// 1
// function stepMessage(){
//     alert("text");
// }

// 2
// function step(obj){
//     alert(obj.href);
// }

// 3 ვიღებთ მოვლენის ტიპს
// function step(e){
//     alert(e.type);
// }

// 4
// function rectStep(e){
//     let date = new Date();
//     let hour = date.getHours();
//     console.log(hour);
//     if(hour>12){
//         e.preventDefault();
//         document.write("12 საათის შემდეგ ვერ შეძლებთ შესვლას");
//     }
// }
// let rect=document.getElementById("rect");
// rect.addEventListener("click",rectStep);

// 5
// function setColor(e){
//     if(e.type === " mouseover"){
//         e.target.style.backgroundColor="yellow";
//     }else if(e.type === " mouseout"){
//         e.target.style.backgroundColor="blue";
//     }

//     let blueStep = document.documentElementById("blueStep");
//     blueStep.addEventListener("mouseover",setColor);
//     blueStep.addEventListener("mouseout",setColor);
// }

// 6
function MoveRect(e){
    let blueStep=document.getElementById("blueStep");
    let cs = window.getComputedStyle(blueStep);
    let left=parseInt(cs.marginLeft);
    let top=parseInt(cs.marginTop);
    switch(e.keyCode){
        case 37: 
        if(left>0)
        blueStep.style.marginLeft=left-10+"px";
        break;
        case 38: 
        if(top>0)
        blueStep.style.marginTop=top-10+"px";
        break;
        case 39: 
        if(left<document.documentElement.clientWidth-100)
        blueStep.style.marginLeft=left+10+"px";
        break;
        case 40:
        if(top<document.documentElement.clientHeight-100)
        blueStep.style.marginTop=top+10+"px";
        break;
    }
}
addEventListener("keydown",MoveRect);