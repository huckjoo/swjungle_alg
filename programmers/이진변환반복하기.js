function solution(s) {
  let totalChange = 0;
  let totalZero = 0;
  const change = (str,num,zeros) =>{
      let cntZero = 0;
      for(let i=0;i<str.length;i++){
          if (str[i]==='0'){
              cntZero+=1;
          }
      }
      const number = str.length-cntZero;
      if (number === 1){
          totalChange = num;
          totalZero = zeros+cntZero
          return;
      }else{
          const binary = number.toString(2);
          change(binary,num+1,zeros+cntZero);
      }
  }
  change(s,1,0);
  return [totalChange,totalZero];
}