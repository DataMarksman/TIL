<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm @create-todo="createTodo"/>
    
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
    },
    // 여기의 todo는 두번 올라온 todo 이다. 이쪽이 중요
    deleteTodo: function (todo) {
      // indexOf 로 인덱스 값 빼오고
      const index = this.todos.indexOf(todo)
      // 자스 문법: splice로 index(인덱스)에 있는 것을 1(한개) 대체 한다.
      this.todos.splice(index, 1)
    }
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
