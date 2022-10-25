const body = document.querySelector('body')
const obj = {
  logThis: function () {
    console.log(this)
  },
  setTime: function () {
    setTimeout(this.logThis, 2000)
  },
  // 이벤트 리스터에서 화살표 함수 사용? -> this가 윈도우로 튕겨나간다.
  // 이부분은 이미 이벤트 리스터가 this를 잡아주기 때문
  addEvents: function () {
    body.addEventListener('click', this.logThis)
  }
}

// forEach 같은 경우
const obj2 = {
  method:function() {
    [1, 2, 3],forEach(function() {
      console.log(this)
    }, this) // 두번째 인자로 this를 넣어주면, method f를 가리키게 됨
    // 만약 이거 없으면 윈도우를 가리킴
  }
}

obj.logThis()
obj.setTime()
obj.addEvents()