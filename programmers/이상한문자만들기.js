function solution(s) {
  let answer = '';
  let splited = s.split(' ');
  s = splited.join('')
  for(let i=0;i<s.length;i++){
      if (i%2===0){
          answer += s[i].toUpperCase();
      }else{
          answer += s[i]
      }
  }
  return answer;
}