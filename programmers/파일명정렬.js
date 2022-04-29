function solution(files) {
  files.sort((a,b)=>{
      let headA = a.match(/\D+/)[0].toUpperCase();
      let headB = b.match(/\D+/)[0].toUpperCase();
      if (headA < headB){
          return -1;
      }else if(headA > headB){
          return 1;
      }else{
          let numA = Number(a.match(/\d+/)[0]);
          let numB = Number(b.match(/\d+/)[0]);
          return numA-numB;
      }
  })
  return files
}