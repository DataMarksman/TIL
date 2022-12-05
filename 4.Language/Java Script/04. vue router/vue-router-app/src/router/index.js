import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'


Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    // 기본 방식. 처음에 컴포넌트 다 가져와유.
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    // lazy-loading: 첫 로딩에 랜더링 하지 않고, 해당 라우터가 동작 할 때, 컴포넌트를 랜더링 한다.
    // 요컨데 지연 로딩. 처음에는 안가져오고, 이게 동작할 때, 불러와서 효율화 추구.
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({ name: 'home'})
      } else {
        next()
      }
    }
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = false

//   // const authPages = ['hello', 'home', 'about']

//   const allowAllPages = ['login']

//   const isAuthRequired = !allowAllPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     next({name: 'login'}) 
//   } else {
//     next()
//   }
// })



export default router
