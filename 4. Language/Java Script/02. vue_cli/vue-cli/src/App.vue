<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/>
    <!-- 3. 보여주기, 이때, prop-data-name은 케밥 케이스로 넣어주자. 어짜피 HTML이 읽을 자료임 -->
    <!-- 이 경우에는 msg를 message-title 같이 표기해줘야 함 -->
    <HelloWorld msg-title ="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// < component 등록 절차 >
// 1. 불러오기
// import MyComponent from './components/MyComponent.vue';
import MyComponent from '@/components/MyComponent'

export default {
  name: 'App',
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent,

}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
