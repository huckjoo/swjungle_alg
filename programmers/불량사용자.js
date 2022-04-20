function solution(user_id, banned_id) {
  const candi = banned_id.map((banned) =>
    user_id.filter((id) => {
      if (id.length === banned.length) {
        for (let i = 0; i < banned.length; i++) {
          if (banned[i] !== '*' && banned[i] !== id[i]) {
            return false;
          }
        }
        return true;
      } else {
        return false;
      }
    })
  );
  let ansDict = {};
  function dfs(idx = 0, choosed = []) {
    if (idx === candi.length) {
      choosed.sort();
      ansDict[choosed.join('')] = true;
      return;
    }
    candi[idx].forEach((x) => {
      if (!choosed.includes(x)) {
        dfs(idx + 1, [...choosed, x]);
      }
    });
  }
  dfs();
  return Object.keys(ansDict).length;
}
