import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
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
