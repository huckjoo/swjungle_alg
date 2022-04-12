function solution(places) {
  let answer = [];
  let arr = new Array(5);
  
  for(let i=0;i<5;i++){
      for (let j = 0; j < arr.length; j++) {
          arr[j] = places[i][j].split("");
      }
      let flag = 1;
      let dx = [0,0,1,-1];
      let dy = [1,-1,0,0];
      for(let y=0; y<5;y++){
          for(let x=0;x<5;x++){
              let cnt = 0;
              if (arr[y][x]==='P'){
                  const visited = [...arr].map((r) => r.map((c) => 0));
                  const queue = [[y,x]];
                  visited[y][x]=1
                  while(queue.length>0){
                      let [cy,cx] = queue.shift()
                      if (arr[cy][cx] == 'P' && visited[cy][cx]==0){
                          flag = 0;
                      }
                      visited[cy][cx]=1
                      for(let k=0;k<4;k++){
                          let ny = cy+dy[k];
                          let nx = cx+dx[k];
                          if (ny>=0 && ny<=4 && nx>=0 && nx<=4){
                              if(arr[ny][nx]!='X' && visited[ny][nx]==0){
                                  if(Math.abs(ny-y)+Math.abs(nx-x)<=2){
                                      queue.push([ny,nx])    
                                  }
                              }
                          }
                      }
                  } 
              }
          }
      }
      answer.push(flag)
  }    
  return answer;
}