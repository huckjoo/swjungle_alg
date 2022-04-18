localStorage.setItem('name', 'Dcron');
console.log(localStorage.getItem('name')); // Dcron

localStorage.removeItem('name');
console.log(localStorage.getItem('name')); // null

sessionStorage.setItem('name', 'dk');
console.log(sessionStorage.getItem('name')); // dk
sessionStorage.setItem('name', 'ohmickey');
console.log(sessionStorage.getItem('name')); // ohmicky

document.cookie = 'name=Kwon; expires=' + new Date(2022, 4, 20).toUTCString();

document.cookie = 'lastName=Moo; expires=' + new Date(2022, 4, 20).toUTCString();

console.log(document.cookie); // name=Kwon; lastName=Moo
