function solution(relation) {
  const keys = [];
  const totalAttrCount = relation[0].length;
  const indexList = Array.from(Array(totalAttrCount), (x, index) => index);

  const isUnique = (relation, attrIndexComb) => {
    let result = Array.from(Array(relation.length), (x) => '');
    for (const attrIndex of attrIndexComb) {
      relation.forEach((row, rowIndex) => (result[rowIndex] += row[attrIndex]));
    }
    return result.length === [...new Set(result)].length;
  };

  const isMinimal = (attrComb) => {
    for (const key of keys) if (key.every((attr) => attrComb.includes(attr))) return false;
    return true;
  };

  for (let attrCount = 1; attrCount <= totalAttrCount; attrCount++) {
    const combinations = getCombinations(indexList, attrCount);
    for (const attrComb of combinations) {
      if (isMinimal(attrComb) && isUnique(relation, attrComb)) keys.push(attrComb);
    }
  }

  return keys.length;
}

const getCombinations = (array, selectNumber) => {
  const result = [];
  if (selectNumber === 1) {
    return array.map((element) => [element]);
  }
  array.forEach((fixed, index, origin) => {
    const restCombinations = getCombinations(origin.slice(index + 1), selectNumber - 1);
    const attached = restCombinations.map((restCombination) => [fixed, ...restCombination]);
    result.push(...attached);
  });
  return result;
};
