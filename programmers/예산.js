function solution(d, budget) {
  let sortedArr = d.sort((a, b) => a - b);
  let left = budget;
  let cnt = 0;
  for (x of sortedArr) {
    left = left - x;
    if (left >= 0) {
      cnt += 1;
    } else {
      break;
    }
  }
  return cnt;
}
