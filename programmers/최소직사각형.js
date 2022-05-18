function solution(sizes) {
  const longs = [];
  const shorts = [];
  for(let i=0;i<sizes.length;i++){
      if (sizes[i][0] > sizes[i][1]){
          longs.push(sizes[i][0]);
          shorts.push(sizes[i][1]);
      }else{
          longs.push(sizes[i][1]);
          shorts.push(sizes[i][0]);
      }
  }
  const maxS = Math.max(...shorts);
  const maxL = Math.max(...longs);
  return maxS * maxL
}