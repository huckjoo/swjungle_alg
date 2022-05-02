function solution(begin, target, words) {
  let candis = [];
  let visited = new Array(words.length).fill(false);
  const canChange = (current, word) => {
    let flag = 0;
    for (let i = 0; i < current.length; i++) {
      if (current[i] !== word[i]) {
        flag += 1;
      }
    }
    if (flag === 1) {
      return true;
    } else {
      return false;
    }
  };
  const dfs = (current, target, cnt) => {
    console.log(current, cnt, candis);
    if (current === target) {
      candis.push(cnt);
      return;
    }
    for (let i = 0; i < words.length; i++) {
      if (canChange(current, words[i]) && visited[i] === false) {
        visited[i] = true;
        dfs(words[i], target, cnt + 1);
        visited[i] = false;
      }
    }
  };
  dfs(begin, target, 0);
  if (candis.length === 0) {
    return 0;
  }
  return Math.min(...candis);
}
