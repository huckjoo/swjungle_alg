function solution(clothes) {
  let dict = {};
  for (let i = 0; i < clothes.length; i++) {
    if (dict[clothes[i][1]] != null) {
      dict[clothes[i][1]] += 1;
    } else {
      dict[clothes[i][1]] = 1;
    }
  }
  console.log(dict);
  valArr = Object.values(dict);
  let ans = 1;
  for (let i = 0; i < valArr.length; i++) {
    ans *= valArr[i] + 1;
  }
  return ans - 1;
}
