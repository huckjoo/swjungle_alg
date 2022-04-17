const targetStr = 'Is this all there is?';

// 문자열 is를 대소문자를 구별하여 한번만 검색한다.
let regexr = /is/;

console.log(targetStr.match(regexr));
// [ 'is', index: 5, input: 'Is this all there is?', groups: undefined ]

// 문자열 is를 대소문자를 구별하지 않고 대상 문자열 끝까지 검색한다.
regexr = /is/gi;

console.log(targetStr.match(regexr)); // [ 'Is', 'is', 'is' ]
console.log(targetStr.match(regexr).length); // 3

// 줄바꿈이 포함된 문자열을 만듭니다.
let str = '\nIs th\nis it?';
console.log(str.match(/^is/m)); // is
// `` 는 "",''과 달리 개행문자를 포함하여 문자열 구성 가능.
str = `abc
addc`;
// 한줄만 검사합니다.
console.log(str.match(/c$/g)); // ["c"]
// 줄마다 검사합니다.
console.log(str.match(/c$/gm)); // (2) ["c", "c"]
