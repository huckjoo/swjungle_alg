// function getCombinations(array, num) {
//   let result = [];
//   if (num === 1) {
//     return array.map((e) => [e]);
//   }
//   array.forEach((fixed, idx, origin) => {
//     let restCombinations = getCombinations(origin.slice(idx + 1), num - 1);
//     let attached = restCombinations.map((restCombination) => [fixed, ...restCombination]);
//     result.push(...attached);
//   });
//   return result;
// }

// console.log(getCombinations([1, 2, 3], 2));

const relation = [
  ['100', 'ryan', 'music', '2'],
  ['200', 'apeach', 'math', '2'],
  ['300', 'tube', 'computer', '3'],
  ['400', 'con', 'computer', '4'],
  ['500', 'muzi', 'music', '3'],
  ['600', 'apeach', 'music', '2'],
];

attrIndexComb = [0, 1];

const isUnique = (relation, attrIndexComb) => {
  let result = Array.from(Array(relation.length), (x) => '');
  for (const attrIndex of attrIndexComb) {
    relation.forEach((row, rowIndex) => (result[rowIndex] += row[attrIndex]));
  }
  return result.length === [...new Set(result)].length;
};
console.log(isUnique(relation, attrIndexComb));
