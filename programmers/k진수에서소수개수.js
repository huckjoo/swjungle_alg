function solution(n, k) {
  let cnt = 0;
  const changed = n.toString(k);
  const splited = changed.split('0');
  const isPrime = (num) =>{
      if (num===0){
          return false;
      }
      if (num===1){
          return false;
      }
      if(num===2){
          return true;
      }
      for(let i=2;i<=Math.sqrt(num);i++){
          if (num%i===0){
              return false;
          }
      }
      return true;
  }
  for(x of splited){
      const num = Number(x);
      if (isPrime(num)===true){
          cnt+=1;
      }
  }
  return cnt;
}