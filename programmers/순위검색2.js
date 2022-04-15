function solution(info, query) {
  let map = {};
  function makeCombination(dataArr, score, map, start) {
    let key = dataArr.join('');
    if (map[key] === undefined) {
      map[key] = [Number(score)];
    } else {
      map[key].push(Number(score));
    }
    for (let i = start; i < 4; i++) {
      let info = [...dataArr]; //얕은복사를 진행
      info[i] = '-';
      makeCombination(info, score, map, i + 1);
    }
  }
  function binarySearch(key, map, minScore) {
    if (map[key] === undefined) {
      return 0;
    }
    let sortedArr = map[key];
    let start = 0;
    let end = sortedArr.length;
    while (start < end) {
      let mid = Math.floor((start + end) / 2); //이것도 왜 floor
      if (sortedArr[mid] >= minScore) {
        end = mid;
      } else {
        start = mid + 1;
      }
    }
    return sortedArr.length - start;
  }
  let answer = [];

  for (let i = 0; i < info.length; i++) {
    let dataArr = info[i].split(' ');
    let score = dataArr.pop();
    makeCombination(dataArr, score, map, 0);
  }

  for (let key in map) {
    //sort를 binary search 안에서 하면 시간초과
    map[key].sort((a, b) => a - b);
  }
  for (let i = 0; i < query.length; i++) {
    let qArr = query[i].replace(/ and /g, ' ').split(' ');
    let minScore = qArr.pop();
    answer.push(binarySearch(qArr.join(''), map, minScore));
  }

  return answer;
}
