const koooo = 'kooookooookoko';
console.log(koooo.match(/ko+/)); // [ 'koooo', index: 0, input: 'kooookooooko', groups: undefined ]
console.log(koooo.match(/(ko)+/)); // [ 'ko', 'ko', index: 0, input: 'kooookooooko', groups: undefined ]
console.log(koooo.match(/(?:ko)+/)); // [ 'ko', index: 0, input: 'kooookooooko', groups: undefined ]
console.log(koooo.match(/(?:ko)+/g)); // [ 'ko', 'ko', 'ko' ]
