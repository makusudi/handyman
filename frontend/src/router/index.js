import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Tasks from '@/components/Tasks'
import Storage from '@/components/Storage'
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
      path: '/dummy',
      name: 'Dummy',
      component: Tasks
    },
    {
      path: '/storage',
      name: 'Storage',
      component: Storage
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
