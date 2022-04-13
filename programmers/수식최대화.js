function solution(expression) {
  let orderArr = [
    ['*', '+', '-'],
    ['*', '-', '+'],
    ['+', '*', '-'],
    ['+', '-', '*'],
    ['-', '+', '*'],
    ['-', '*', '+'],
  ];
  let ansArr = [];
  for (curr of orderArr) {
    let splited = expression.split(/(\D)/);
    for (operator of curr) {
      while (splited.indexOf(operator) !== -1) {
        let idx = splited.indexOf(operator);
        splited.splice(idx - 1, 3, eval(splited.slice(idx - 1, idx + 2).join('')));
      }
    }
    ansArr.push(Math.abs(splited));
  }
  return Math.max(...ansArr);
}
