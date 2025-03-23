User("hatsunemiku2007"); // здесь пишите логин 
password(123456789);

function User() { // данные
    console.log("hatsunemiku2007"); // здесь пишите пароль
};
setTimeout(() => {
   console.log(User.name)
   console.log(password.name)
},  1000);
function password() {  
    console.log(123456789);
};