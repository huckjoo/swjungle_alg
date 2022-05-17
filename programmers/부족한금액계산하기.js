function solution(price, money, count) {
  let target = 0;
  for (let i = 1; i <= count; i++) {
    target += i;
  }
  if (target * price <= money) {
    return 0;
  } else {
    return target * price - money;
  }
}
