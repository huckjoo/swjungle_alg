let x = 1;

function first() {
  // 전역에서 선언
  console.log(x); // undefined
  let x = 10;
  second();
  console.log(x, 'x'); // 10
}

function second() {
  // 전역에서 선언
  console.log(x);
}

first(); // 1
second(); // 1
