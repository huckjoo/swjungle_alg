function solution(citations) {
  let cnt = 0;
  let answer = 0;
  let hArr = [];
  let max = Math.max(...citations);
  let min = Math.min(...citations);
  for (let i = 0; i <= max; i++) {
    cnt = 0;
    for (let j = 0; j < citations.length; j++) {
      if (i <= citations[j]) {
        cnt += 1;
      }
    }
    if (cnt >= i) {
      hArr.push(i);
    }
  }
  let ans = Math.max(...hArr);
  return ans;
}
let citations = [3, 0, 6, 1, 5];
console.log(solution(citations));
