function solution(dartResult) {
  let answer = 0;
  let arr = [];
  for (let i=0;i<dartResult.length;i++){
      if (!isNaN(dartResult[i])){ // 숫자
          if (dartResult[i]==='1' && dartResult[i+1]==='0'){
              arr.push(10);
              i=i+1;
          }else{
              arr.push(Number(dartResult[i]));    
          }
      }
      console.log(i)
      if(dartResult[i]==='D'){
          arr[arr.length-1] = (arr[arr.length-1])**2;
      }
      if(dartResult[i]==='T'){
          arr[arr.length-1] = (arr[arr.length-1])**3;
      }
      if (dartResult[i]==='#'){
          arr[arr.length-1] = arr[arr.length-1]*(-1);
      }
      if(dartResult[i]==='*'){
          arr[arr.length-1] = arr[arr.length-1]*2;
          if(arr.length>1){
              arr[arr.length-2] = arr[arr.length-2]*2
          }
      }
  }
  for(let i=0;i<arr.length;i++){
      answer+=arr[i]
  }
  return answer;
}