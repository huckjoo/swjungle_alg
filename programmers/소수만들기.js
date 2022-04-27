function solution(nums) {
  const isPrime = (num) => {
      if (num===1){
          return false;
      }
      if(num===2){
          return true;
      }
      for(let i=2;i<num;i++){
          if (num%i===0){
              return false;
          }
      }
      return true;
  }
  const getCombinations = (arr,selectNumber)=>{
      const results = [];
      if(selectNumber === 1) return arr.map((value)=>[value]);
      
      arr.forEach((fixed,index,origin)=>{
          const rest = origin.slice(index+1);
          const combinations = getCombinations(rest,selectNumber-1)
          const attached = combinations.map((combination)=>[fixed,...combination]);
          results.push(...attached);
      });
      return results;
  }
  const newArr = getCombinations(nums,3).map(x=>{
      let sum = 0;
      x.forEach(ele=>sum+=ele);
      return sum
  })
  let answer = 0;
  newArr.forEach(x=>{
      if(isPrime(x)){
        answer+=1   
      }
  })
  return answer;
}