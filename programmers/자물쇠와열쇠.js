function solution(key, lock) {
  function isTrue(arr, len) {
    for (let y = len; y < len * 2; y++) {
      for (let x = len; x < len * 2; x++) {
        if (arr[y][x] !== 1) {
          return false;
        }
      }
    }
    return true;
  }

  let N = lock[0].length;
  let M = key[0].length;

  const bigArr = Array.from(Array(N * 3), () => Array(N * 3).fill(0));

  for (let y = 0; y <= N - 1; y++) {
    for (let x = 0; x <= N - 1; x++) {
      bigArr[y + N][x + N] = lock[y][x]; // 가운데에 lock 삽입
    }
  }

  for (let i = 0; i < 4; i++) {
    // key 90도 회전 4번
    key = key[0].map((val, index) => key.map((row) => row[index]).reverse());
    // 순회하면서 lock을 key에 비교
    for (let y = 0; y <= bigArr.length - M; y++) {
      for (let x = 0; x <= bigArr.length - M; x++) {
        let newArr = bigArr.map((row) => [...row]);
        for (let b = 0; b < M; b++) {
          for (let a = 0; a < M; a++) {
            newArr[y + b][x + a] += key[b][a];
          }
        }
        if (isTrue(newArr, N)) {
          return true;
        }
      }
    }
  }
  return false; // 다 해봤는데 안될 때
}
