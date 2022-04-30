function solution(msg) {
  let ans = [];
  let dict = new Array(27).fill().map((_,i)=>String.fromCharCode(i+64));
  for(let i=0,j;i<msg.length;i=j){
      let w = msg[i];
      for(j = i+1;j<msg.length;j++){
          let c = msg[j];
          if (!dict.includes(w+c)){
              dict.push(w+c);
              break;
          }
          w = w+c
      }
      ans.push(dict.indexOf(w))
  }
  return ans;
}