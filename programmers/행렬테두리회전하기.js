function solution(rows, columns, queries) {
  let answer = [];
  // board 만들기
  const board = Array.from(Array(rows), () => Array(columns).fill(null));
  let value = 1;
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < columns; x++) {
      board[y][x] = value;
      value += 1;
    }
  }
  // 회전하는 거 구현
  for (let query of queries) {
    let [x1, y1, x2, y2] = query.map((x) => x - 1);
    let temp = board[x1][y1];
    let min = temp;
    console.log(x1, y1, x2, y2, temp);
    // 좌
    for (let i = x1; i < x2; i++) {
      board[i][y1] = board[i + 1][y1];
      if (min > board[i][y1]) {
        min = board[i][y1];
      }
    }
    // 하
    for (let i = y1; i < y2; i++) {
      board[x2][i] = board[x2][i + 1];
      if (min > board[x2][i]) {
        min = board[x2][i];
      }
    }
    // 우
    for (let i = x2; i > x1; i--) {
      board[i][y2] = board[i - 1][y2];
      if (min > board[i][y2]) {
        min = board[i][y2];
      }
    }
    // 상
    for (let i = y2; i > y1; i--) {
      board[x1][i] = board[x1][i - 1];
      if (min > board[x1][i]) {
        min = board[x1][i];
      }
    }
    board[x1][y1 + 1] = temp;
    answer.push(min);
  }
  return answer;
}
