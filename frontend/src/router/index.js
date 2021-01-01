import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Tasks from '@/components/Tasks'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/tasks',
      name: 'Tasks',
      component: Tasks
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
