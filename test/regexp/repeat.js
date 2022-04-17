const target = 'A AA B BB Aa Bb AAA';
const regExp = /[AB]+/g;
console.log(target.match(regExp));

const expression = '100-200*300-500+20';
let splited = expression.split(/(\D)/g);

console.log(splited);
