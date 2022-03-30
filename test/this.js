let someone = {
  name: 'Dcron',
  whoAmI: function () {
    console.log(this);
  },
};

someone.whoAmI();

let myWhoAmI = someone.whoAmI;
myWhoAmI();

let bindedWhoAmI = myWhoAmI.bind(someone);

const btn = document.querySelector('#btn');
// btn.addEventListener('click', someone.whoAmI);
btn.addEventListener('click', bindedWhoAmI);
