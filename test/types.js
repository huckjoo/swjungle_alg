// 변수를 각각 선언하여 두 변수의 참조 값이 다른 상황.
let a = [1, 2];
let b = [1, 2];
console.log(a === b); // false

// 두 변수의 참조 값이 같은 상황.
let c = [1, 2];
let d = c;
console.log(c === d); // true

let e = [1, 2, 3];
let f = e;
f[0] = 8;
console.log(f);
console.log(e);
console.log(e === f); // true
