function solution(gems) {
  let ans = [1, gems.length];
  let cnt = new Set(gems).size;
  let l = 0;
  let r = 0;
  let hit = new Map();
  hit.set(gems[l], 1);
  while (r < gems.length) {
    if (cnt === hit.size) {
      // 조건 만족
      if (ans[1] - ans[0] > r - l) {
        ans = [l + 1, r + 1];
      }
      hit.set(gems[l], hit.get(gems[l]) - 1);
      if (hit.get(gems[l]) === 0) {
        hit.delete(gems[l]);
      }
      l++;
    } else {
      r++;
      if (hit.get(gems[r]) === undefined) {
        hit.set(gems[r], 1);
      } else {
        hit.set(gems[r], hit.get(gems[r]) + 1);
      }
    }
  }
  return ans;
}
