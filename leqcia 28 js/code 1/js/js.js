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


function User(pName,pAge){
    this.name=pName;
    this.Page=pAge;
    this.stepInfo=function(){
        document.write("სახელი",this.name+"ასაკი"+"<br>");
    };
};

User.prototype.hello=function(){
    document.write(this.name+"ამბობს'გამარჯობა'!<br>");
};

User.prototype.maxAge=110;
let lia=new User("ლია",30);
lia.hello();
let lado=new User("ლადო",24);
lia.maxAge=99;
lado.hello();
console.log(lia.maxAge);
console.log(lado.maxAge);