function solution(m, n, board) {
  board = board.map((row) => row.split(''));
  const isSame = (y, x) => {
    if (board[y][x] && board[y][x] === board[y + 1][x] && board[y][x] === board[y][x + 1] && board[y][x] === board[y + 1][x + 1]) {
      return true;
    } else {
      return false;
    }
  };
  const remover = (canRemove) => {
    for ([y, x] of canRemove) {
      if (y + 1 <= m && x + 1 <= n) {
        board[y][x] = 0;
        board[y + 1][x] = 0;
        board[y][x + 1] = 0;
        board[y + 1][x + 1] = 0;
      }
    }
  };
  const update = () => {
    for (let y = m - 1; y >= 0; y--) {
      for (let x = n - 1; x >= 0; x--) {
        if (board[y][x]) continue;
        let idx = y - 1;
        while (idx > -1) {
          if (board[idx][x] !== 0) {
            board[y][x] = board[idx][x];
            board[idx][x] = 0;
            break;
          } else {
            idx--;
          }
        }
      }
    }
  };
  while (true) {
    let canRemove = [];
    for (let y = 0; y < m - 1; y++) {
      for (let x = 0; x < n - 1; x++) {
        if (isSame(y, x)) {
          canRemove.push([y, x]);
        }
      }
    }
    if (canRemove.length === 0) {
      // 지울 프렌즈들 없음
      break;
    }
    remover(canRemove);
    update();
  }
  let cnt = 0;
  board.map((row) => {
    row.map((ele) => {
      if (ele === 0) {
        cnt++;
      }
    });
  });
  return cnt;
}
