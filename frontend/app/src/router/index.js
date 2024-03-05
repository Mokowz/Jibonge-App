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
  },
  {
    path: '/blog/:id',
    name: 'blog',
    component: () => import('../views/Blogs/Blog.vue')
  },
  {
    path: '/tags',
    name: 'tags',
    component: () => import('../views/Tags/Tags.vue')
  },
  {
    path: '/tag/:id',
    name: 'tagsList',
    component: () => import('../views/Tags/TagBlogs.vue')
  },
  {
    path: '/new/blog',
    name: 'newBlog',
    component: () => import('../views/Blogs/NewBlog.vue')
  },
  {
    path: '/authors',
    name: 'authors',
    component: () => import('../views/Authors/Authors.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
