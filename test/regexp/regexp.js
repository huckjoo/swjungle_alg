const regex = /\d{3}-\d{4}-\d{4}/;
// \d는 숫자를 의미하고, {}안의 숫자는 개수를 의미

console.log(regex.test('010-1234-5678')); // true
console.log(regex.test('01012345678')); // flase;
