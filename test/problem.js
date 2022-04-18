function outerFunc() {
  var x = 10;
  var innerFunc = function () {
    console.log(x);
    x++;
  };
  return innerFunc;
}

var inner = outerFunc();
inner();
inner();
inner();
