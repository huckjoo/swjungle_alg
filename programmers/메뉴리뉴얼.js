function solution(orders, course) {
  let ans = [];
  const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);
    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = getCombinations(rest, selectNumber - 1);
      const attached = combinations.map((el) => [fixed, ...el].sort().join(''));
      results.push(...attached);
    });
    return results;
  };
  for (let i = 0; i < course.length; i++) {
    let dict = {};
    for (let j = 0; j < orders.length; j++) {
      arr = orders[j].split('');
      getCombinations(arr, course[i]).forEach((x) => {
        if (dict[x] === undefined) {
          dict[x] = 1;
        } else {
          dict[x] += 1;
        }
      });
    }
    let maximum = -1;
    let maximumVal = '';
    for (let key of Object.keys(dict)) {
      if (maximum < dict[key]) {
        maximum = dict[key];
      }
    }
    for (let key of Object.keys(dict)) {
      if (maximum == dict[key] && maximum >= 2) {
        ans.push(key);
      }
    }
  }

  return ans.sort();
}
