import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Tasks from '@/components/Tasks'

Vue.use(Router)

export default new Router({
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
    }
  ]
})
