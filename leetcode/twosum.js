var twoSum = function (nums, target) {
  // for(let i=0;i<nums.length;i++){
  //     for(let j=i+1;j<nums.length;j++){
  //         if(nums[i]+nums[j]===target){
  //           return [i,j]
  //         }
  //     }
  // }
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    const another = target - nums[i];
    if (another in map) {
      return [map[another], i];
    } else {
      map[nums[i]] = i;
    }
  }
};
