// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import SocketIO from 'vue-socket.io'

Vue.use(ElementUI)

Vue.use(new SocketIO({
  debug: true,
  connection: `ws://localhost:8000/`,
  // transports: ['websocket'],
  options: {
    upgrade: true,
    // path: '/io/socket.io',
    reconnection: true,
    autoConnect: true,
    transports: ['websocket', 'polling']
  }
}))

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
