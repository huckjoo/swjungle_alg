function solution(begin, target, words) {
  let n = words.length;
  let visited = new Array(n).fill(false);
  let ansArr=[]
  function DFS(L,now){
      if (L==n){
          return
      }
      if(now == target){
          ansArr.push(L)
      }
      for(let i=0; i<n;i++){
          let flag=0;
          for(let j=0; j<begin.length;j++){
              if (now[j] != words[i][j]){
                  flag+=1
              } 
          }
          if (visited[i]==false && flag == 1){
              visited[i]=true
              DFS(L+1,words[i])
              visited[i]=false
          }
      }
  }
  DFS(0,begin); // DFS 시작
  if (ansArr.length == 0){
      return 0
  }else{
      return Math.min(...ansArr)
  }
}