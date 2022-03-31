function solution(s) {
  if (s.length % 2 === 1) {
    return 0;
  }
  let ans = 0;
  let arr = s.split('');
  let stack = [];
  while (arr.length > 0) {
    let curr = arr.pop();
    if (stack.length > 0 && stack[stack.length - 1] === curr) {
      stack.pop();
    } else {
      stack.push(curr);
    }
  }
  if (stack.length === 0) {
    ans = 1;
  }
  return ans;
}
