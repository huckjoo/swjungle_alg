function solution(n, computers) {
  let visited = new Array(n).fill(false);
  const DFS = (idx) => {
      visited[idx]=true;
      for(let i=0;i<n;i++){
          if(computers[idx][i]===1 && idx!==i && visited[i]===false){
              DFS(i);
          }
      }
  }
  let cnt = 0;
  for(let i=0;i<n;i++){
      if (visited[i]===false){
          DFS(i);
          cnt++;
      }
  }
  return cnt
}