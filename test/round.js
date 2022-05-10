// 그냥 round는 1.005를 정확히 반올림하지 못함
const num = 1.005;
console.log(Math.round(num * 100) / 100);

// 반올림 예외처리 막기
const roundToTwo = (num) => {
  return +(Math.round(num + 'e+2') + 'e-2');
};
console.log(roundToTwo(1.005));
