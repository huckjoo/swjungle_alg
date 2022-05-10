dict = {
  1: 1,
  11: 11,
  103: 103,
  2: 2,
  3: 3,
};
let ans = [];
for (x of Object.keys(dict)) {
  ans.push(dict[x]);
}
console.log(ans); // Object.keys 순서 보장되는지 찾아보기
