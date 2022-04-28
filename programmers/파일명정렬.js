function solution(files) {
  return files.sort((a,b)=>{
      const headA = a.match(/\D+/)[0].toUpperCase();
      const headB = b.match(/\D+/)[0].toUpperCase();
      if(headA < headB){
          return -1;
      }
      if(headA > headB){
          return 1;
      }
      // headA와 headB가 같다면
      const numberA = Number(a.match(/\d+/)[0]);
      const numberB = Number(b.match(/\d+/)[0]);
      return numberA - numberB
  })
}