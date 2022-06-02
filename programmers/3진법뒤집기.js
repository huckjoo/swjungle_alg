function solution(n) {
  let ans = 0;
  const arr = [];
  while(n>=1){
      arr.push(n%3);
      n = Math.floor(n/3)
  }
  const thirdString = arr.join('');
  for(let i=0;i<thirdString.length;i++){
      ans += Number(thirdString[i])*(3**(thirdString.length-i-1));
  }
  return ans
}