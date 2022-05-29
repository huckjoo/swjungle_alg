const array = Array.from(Array(3), () => Array(3).fill(0));
const newArr = [...array];

console.log(array === newArr); // false
console.log(array[0] === newArr[0]); // true

array[0][0] = 100;
console.log(array, 'original');

console.log(newArr, 'new');
