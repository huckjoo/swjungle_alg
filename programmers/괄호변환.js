function solution(p) {
  if (p.length === 0){
      return ''
  }
  let cnt = 0;
  let flag = 0;
  let ans = ''
  for(let i=0;i<p.length;i++){
      if (p[i] === '('){
          cnt += 1
      }else{
          cnt -= 1
      }
      if (cnt<0){
          flag=1;
      }
      if (cnt===0){ // 균형잡힌 괄호 문자열
          u = p.slice(0,i+1);
          v = p.slice(i+1);
          if (flag ===0){//u가 올바른 문자열
              ans = u+solution(v);
              return ans;
          }else{
              ans += '(';
              ans = ans + solution(v) + ')';
              for(let j=1;j<i;j++){
                  if (p[j]==="("){
                      ans+=')'
                  }else{
                      ans+='('
                  }
              }
              return ans;
          }
      }
  }
}