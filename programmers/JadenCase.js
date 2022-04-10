function solution(s) {
  let arr = s.split(" ")
  console.log(arr,"split 후")
  let ans = arr.map(function(x){
      if(isNaN(x[0]) && x!=""){ // 영문자일때
          x = x.toLowerCase();
          x = x.replace(x[0],x[0].toUpperCase())
          return x
      }else if(!isNaN(x[0]) && x!=""){ // 앞에 하나가 숫자일때 
          x = x.toLowerCase();
          return x
      }else{
          return x
      }
  })
  return ans.join(" ");
}