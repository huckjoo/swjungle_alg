function solution(cacheSize, cities) {
  let answer = 0;
  if (cacheSize === 0) {
    return cities.length * 5;
  }
  let cache = [];
  function hit(city) {
    for (let i = 0; i < cache.length; i++) {
      if (cache[i] === city) {
        return true;
      }
    }
    return false;
  }
  for (let city of cities) {
    city = city.toUpperCase();
    if (cache.length < cacheSize) {
      // 자리가 빈 경우
      if (hit(city)) {
        // 이미 있는경우
        let targetIdx = cache.indexOf(city);
        let target = cache.splice(targetIdx, 1);
        cache.push(target[0]);
        answer += 1;
      } else {
        answer += 5;
        cache.push(city);
      }
    } else if (cache.length === cacheSize) {
      if (hit(city)) {
        // 이미 있는경우
        answer += 1;
        let targetIdx = cache.indexOf(city);
        let target = cache.splice(targetIdx, 1);
        cache.push(target[0]);
      } else {
        answer += 5;
        cache.shift();
        cache.push(city);
      }
    }
  }
  return answer;
}
