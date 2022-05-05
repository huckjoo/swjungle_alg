function solution(numbers) {
  let ans = [];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      ans.push(numbers[i] + numbers[j]);
    }
  }
  ans = [...new Set(ans)];
  ans.sort((a, b) => a - b);
  return ans;
}
