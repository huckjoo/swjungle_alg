function solution(n, arr1, arr2) {
  let answer = []
  let barr1 = arr1.map(int=>(int).toString(2).padStart(n,0));
  let barr2 = arr2.map(int=>(int).toString(2).padStart(n,0));
  let result = Array.from(Array(n),()=>Array(n).fill(' '));
  for(let y=0; y<n;y++){
      for(let x=0; x<n; x++){
          if (barr1[y][x]==='1' || barr2[y][x]==='1'){
              result[y][x]='#'
          }
      }
  }
  answer = result.map(row=>row.join(''))
  return answer;
}