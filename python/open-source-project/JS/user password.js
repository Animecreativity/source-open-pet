User("hatsunemiku2007"); // здесь пишите логин   это без защиты typescript 
password(123456789); // пишем пароль


function User() { // данные
    console.log("hatsunemiku2007"); //  здесь пишет логин
};
setTimeout(() => {
   console.log(User.name) // в сервер передаёт данные
   console.log(password.name) // в сервер передаёт данные
},  3000);
function password() {  
    console.log(123456789); // пишет пароль
};
