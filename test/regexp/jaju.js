const targetStr = 'abc#123';

// A-Za-z0-9 이외의 문자가 있는지 검사
let regexr = /[^A-Za-z0-9]/gi;

console.log(regexr.test(targetStr)); // true

// 특수 문자 제거
console.log(targetStr.replace(regexr, '')); // abc123

const text = `http://dogumaster.com http://google.com 010-1111-2222 02-333-7777 curryyou@aaa.com`;
console.log(text.match(/https?:\/\/[\w\-\.]+/g));
// [ 'http://dogumaster.com', 'http://google.com' ]
