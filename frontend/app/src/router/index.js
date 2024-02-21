import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignUp/Signup.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LogIn/Login.vue')
  },
  {
    path: '/blogs',
    name: 'blogs',
    component: () => import('../views/Blogs/Blogs.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
