const array = Array.from(Array(3), () => Array(3).fill(0));
const newArr = array.map((row) => [...row]);

console.log(array === newArr); // false
console.log(array[0] === newArr[0]); // false

array[0][0] = 100;
console.log(array, 'original');
//[ [ 100, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ] original
console.log(newArr, 'new');
//[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ] new
