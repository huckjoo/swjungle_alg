//arrow.js
const btn = document.querySelector('#btn');

let myObj = {
  count: 0,
  setCounter: function () {
    console.log(this.count);
    btn.addEventListener('click', () => {
      console.log(this.count++);
    });
  },
};

myObj.setCounter(); // 0
