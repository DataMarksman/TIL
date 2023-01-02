// 1. dash-case(kebab-case) => html, css 사용
// 2. snake_case
// 3. camelCase === lowerCamelCase (JS 주로 활용)
// 4. PascalCase === UpperCamelCase (JS class명)
// 5. UPPER_SNAKE_CASE => 절대 변하면 안될 것 같은 상수들

// < 차이를 살펴 보자 >
// var a
// var = > ES5, 재선언 및 재할당 가능

// let b
// let = > 변수 선언 방식, 재 "할당" 가능 (재 선언 불가능)

// const c
// const = > 재 선언, 재 할당 불가능

let x = 1
x = 2
console.log(x)

// < 변수 호이스팅 >
// = > 나중에 선언해준거를 머리끄댕이 잡고 올려준다.
// JS는 인터프리터가 아니라서 한줄 한줄 읽는게 아니기 때문에 가능.
console.log(foo)
var foo

// 하지만 이런 경우는 불가능 하다.
console.log(bar);
let bar;

