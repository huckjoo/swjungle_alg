function solution(n, t, m, p) {
  let arr = '';
  let ans = '';
  for (let i = 0; i <= (m + 1) * t; i++) {
    arr += i.toString(n);
  }
  arr = arr.toUpperCase();
  let cnt = 1;
  let i = p - 1;
  while (cnt <= t) {
    ans += arr[i];
    i = i + m;
    cnt++;
  }
  return ans;
}
