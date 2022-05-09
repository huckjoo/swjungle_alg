function solution(nums) {
  let n = nums.length;
  let max = n / 2;
  let set = new Set(nums);
  let arr = [...set];
  if (arr.length < max) {
    return arr.length;
  } else {
    return max;
  }
}
