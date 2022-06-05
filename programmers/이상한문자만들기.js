function solution(s) {
  let answer = '';
  let cnt = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') {
      answer += ' ';
      cnt = 0;
    } else {
      if (cnt % 2 === 0) {
        answer += s[i].toUpperCase();
        cnt += 1;
      } else {
        answer += s[i].toLowerCase();
        cnt += 1;
      }
    }
  }
  return answer;
}
