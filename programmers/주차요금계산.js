function solution(fees, records) {
  const ans = [];
  const baseTime = fees[0];
  const baseFee = fees[1];
  const unitTime = fees[2];
  const unitFee = fees[3];
  const dict = {};
  for (let record of records) {
    const splited = record.split(' ');
    const time = splited[0];
    const timeSplited = time.split(':');
    const hour = Number(timeSplited[0]);
    const min = Number(timeSplited[1]);
    const duration = hour * 60 + min;
    const car = splited[1];
    if (dict[car] === undefined) {
      dict[car] = [duration];
    } else {
      dict[car].push(duration);
    }
  }
  const keyArr = Object.keys(dict);
  keyArr.sort((a, b) => {
    if (Number(a) < Number(b)) {
      return -1;
    } else {
      return 1;
    }
  });
  for (let key of keyArr) {
    if (dict[key].length % 2 === 1) {
      dict[key].push(1439);
    }
    let right = 0;
    let left = 0;
    for (let i = 0; i < dict[key].length; i++) {
      if (i % 2 === 0) {
        left += dict[key][i];
      } else {
        right += dict[key][i];
      }
    }
    const totalTime = right - left;
    if (totalTime - baseTime <= 0) {
      ans.push(baseFee);
    } else {
      const result = baseFee + Math.ceil((totalTime - baseTime) / unitTime) * unitFee;
      ans.push(result);
    }
  }
  return ans;
}
