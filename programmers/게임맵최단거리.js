function solution(maps) {
  let queue = [[0, 0]];
  let dy = [0, 0, -1, 1];
  let dx = [1, -1, 0, 0];
  let visited = Array.from(Array(maps.length), () => Array(maps[0].length).fill(0));
  visited[0][0] = 1;
  while (queue.length > 0) {
    let [y, x] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let ny = dy[i] + y;
      let nx = dx[i] + x;
      if (0 > ny || ny >= maps.length || 0 > nx || nx >= maps[0].length) {
        continue;
      }
      if (maps[ny][nx] !== 1 || visited[ny][nx] !== 0) {
        continue;
      }
      maps[ny][nx] = maps[y][x] + 1;
      visited[ny][nx] = 1;
      queue.push([ny, nx]);
    }
  }
  if (maps[maps.length - 1][maps[0].length - 1] === 1) {
    return -1;
  } else {
    return maps[maps.length - 1][maps[0].length - 1];
  }
}
