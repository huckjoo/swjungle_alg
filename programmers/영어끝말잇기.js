function solution(n, words) {
  let answer = [];
  let dict = {};
  dict[words[0]] = 1;
  const isUnique = (i) => {
    if (dict[words[i]] === undefined) {
      dict[words[i]] = 1;
      return true;
    } else {
      return false;
    }
  };
  target = -1;
  for (let i = 1; i < words.length; i++) {
    if (!isUnique(i)) {
      target = i + 1;
      break;
    }
    if (words[i][0] !== words[i - 1][words[i - 1].length - 1]) {
      target = i + 1;
      break;
    }
  }
  if (target === -1) {
    return [0, 0];
  }
  let number = parseInt(target / n);
  let order = target % n;
  if (order === 0) {
    return [n, number];
  } else {
    return [order, number + 1];
  }
}
