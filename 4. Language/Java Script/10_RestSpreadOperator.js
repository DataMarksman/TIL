/* Rest Operator */

function withoutRestOpr(x, y, a, b, c, d, e) {
  console.log(x, y)
  const numbers = [a, b, c, d, e]
  return numbers.map(num => num + 1)
}

// def a(*args)
function withRestOpr(x, y, ...numbers) {
  console.log(x, y)
  return numbers.map(num => num + 1)
}


/* Spread Operator */
// 두 Array를 합쳐주는 기능 수행
// 딱히 번갈아가면서 합쳐주는거 아니니까 기대는 말도록.
function withoutSpreadOpr() {
  const odds = [1, 3, 5, 7]
  const evens = [2, 4, 6, 8]
  const nums = odds.concat(evens)
}


function withSpreadOpr() {
  const odds = [1, 3, 5, 7]
  const evens = [2, 4, 6, 8]
  // python: [*odds, *evens]
  const nums = [...odds, ...evens]
}

console.log(withoutSpreadOpr())


