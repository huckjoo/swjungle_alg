function solution(left, right) {
  let ans = 0;
  const getMatch = (target) => {
    let cnt = 0;
    for (let i = 1; i <= target; i++) {
      if (target % i === 0) {
        cnt += 1;
      }
    }
    return cnt;
  };
  for (let i = left; i <= right; i++) {
    if (getMatch(i) % 2 === 0) {
      ans += i;
    } else {
      ans -= i;
    }
  }
  return ans;
}
