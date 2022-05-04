function solution(tickets) {
  let n = tickets.length;
  let visited = new Array(n).fill(false);
  tickets.sort();
  let ans = [];
  let temp = ['ICN'];
  const DFS = (curr, L, temp) => {
    if (L === n) {
      let t = [...temp];
      ans.push(t);
      return;
    }
    for (let i = 0; i < n; i++) {
      if (tickets[i][0] === curr && visited[i] === false) {
        temp.push(tickets[i][1]);
        visited[i] = true;
        DFS(tickets[i][1], L + 1, temp);
        visited[i] = false;
        temp.pop();
      }
    }
  };
  DFS('ICN', 0, temp);
  ans.sort();
  return ans[0];
}
