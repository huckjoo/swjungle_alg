// 부모 클래스
function MyParent() {
  this.property1 = 'data1';
  console.log('MyParent');
}

MyParent.prototype.method1 = function () {
  console.log('property1 = ' + this.property1);
};

// 자식 클래스
function MyChild() {
  console.log('MyChild');
}

// 부모 클래스 상속하기
MyChild.prototype = new MyParent();

// 생성자 설정
MyChild.prototype.constructor = MyChild;

/** * ------------------ * 메서드 오버라이드 * ------------------ **/
MyChild.prototype.method1 = function () {
  console.log('프로퍼티 1은 = ' + this.property1 + ' 입니다.');
};
// 자식 인스턴스 생성
var child = new MyChild();

// 메서드 호출
child.method1();

console.log(child.property1);

// 콘솔창 결과
// MyParent
// MyChild
// 프로퍼티 1은 = data1입니다.
