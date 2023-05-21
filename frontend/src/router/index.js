import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
// import Login from '../pages/Login.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: Home,
  },
  // {
  //   path: '/login',
  //   name: 'login',
  //   component: Login,
  // },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/home',
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
