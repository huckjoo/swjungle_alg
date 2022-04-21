function solution(relation) {
  let keys = [];
  let totalIdx = Array.from(Array(relation[0].length), (x, i) => i);
  const isUnique = (relation, indexCombis) => {
    const tempArr = Array.from(Array(relation.length), (x) => '');
    relation.forEach((row, idx) => {
      for (const indexCombi of indexCombis) {
        tempArr[idx] += row[indexCombi];
      }
    });
    return tempArr.length === [...new Set(tempArr)].length;
  };
  // keys에 key의 부분집합이 존재하는지 확인
  const isMinimal = (indexCombis) => {
    for (const key of keys) {
      if (key.every((x) => indexCombis.includes(x))) {
        return false;
      }
    }
    return true;
  };

  for (let i = 1; i <= relation[0].length; i++) {
    const currCombis = getCombi(totalIdx, i);
    for (const currCombi of currCombis) {
      if (isMinimal(currCombi) && isUnique(relation, currCombi)) {
        keys.push(currCombi);
      }
    }
  }

  return keys.length;
}
// 조합을 구하는 함수
const getCombi = (array, number) => {
  let result = [];
  if (number === 1) {
    return array.map((e) => [e]);
  }
  array.forEach((fixed, idx, origin) => {
    let restCombis = getCombi(origin.slice(idx + 1), number - 1);
    let attached = restCombis.map((restCombi) => [fixed, ...restCombi]);
    result.push(...attached);
  });
  return result;
};
