// 1. dash-case(kebab-case) => html, css 사용
// 2. snake_case
// 3. camelCase === lowerCamelCase (JS 주로 활용)
// 4. PascalCase === UpperCamelCase (JS class명)
// 5. UPPER_SNAKE_CASE => 절대 변하면 안될 것 같은 상수들

// let = > 변수 선언 방식, 재'할당' 가능 (재선언은 불가능)
let x = 3
x = 4

// const => 안 바뀔만한 것에 쓴다, 재선언 및 재할당 불가능
const y = 3
// y = 12

// var => ES5, 재선언 및 재할당 가능
console.log(foo) // 호이스팅 되어 undefined
var foo;

console.log(bar) // reference error
let bar;



/* 기본 값이 var 라고? 말도 안되는 소리!
+ delete는 figuarble 한 것만 지울 수 있다규~ var는 못 지워~
a = 3
3

var b = 4
undefined

window
Window {0: global, window: Window, self: Window, document: document, name: '', location: Location, …}

Object.getOwnPropertyDescriptor(window, 'a')
{value: 3, writable: true, enumerable: true, configurable: true}configurable: trueenumerable: truevalue: 3writable: true[[Prototype]]: Object

Object.getOwnPropertyDescriptor(window, 'b')
{value: 4, writable: true, enumerable: true, configurable: false}

delete a
true

delete b
false

delete a
true

a
VM337:1 Uncaught ReferenceError: a is not defined
    at <anonymous>:1:1
(anonymous) @ VM337:1

delete a
true

delete b
false

b
4

this.a
undefined

this.b
4
*/