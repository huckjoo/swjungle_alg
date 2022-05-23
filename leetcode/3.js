var lengthOfLongestSubstring = function (s) {
  if (s.length === 0) {
    return 0;
  }
  let leftP = 0;
  let rightP = 1;
  let maxLength = 1;
  let currLength = 1;
  let currSet = new Set();
  currSet.add(s[0]);

  while (leftP < s.length && rightP < s.length && leftP <= rightP) {
    if (!currSet.has(s[rightP])) {
      // 중복 없으면 오른쪽 추가
      currSet.add(s[rightP]);
      rightP += 1;
      currLength += 1;
      if (maxLength < currLength) {
        maxLength = currLength;
      }
    } else if (leftP <= rightP) {
      // 중복 있으면 왼쪽 제거
      currSet.delete(s[leftP]);
      leftP += 1;
      currLength -= 1;
    } else {
      // 둘다 안될 경우
      currSet.delete(s[leftP]);
      leftP += 1;
      currSet.add(s[rightP]);
      rightP += 1;
    }
  }
  return maxLength;
};
