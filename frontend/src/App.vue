<template>
  <div>
    <el-menu
      v-if="true"
      router="true"
      :default-active="'/'"
      class="el-menu-demo px-4"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/">Home</el-menu-item>
      <el-menu-item index="/tasks">Tasks</el-menu-item>
      <el-menu-item index="/chat">Chat</el-menu-item>
    </el-menu>
    <div id="app">
      <transition name="fade">
        <router-view/>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  created () {
    this.$socket.connect()
    window.onbeforeunload = () => {
      this.$socket.disconnect()
    }
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 2rem;
}

.fade-enter-active, .fade-leave-active {
  transition-property: opacity;
  transition-duration: .4s;
}
.fade-enter-active {
  transition-delay: .4s;
}
.fade-enter, .fade-leave-active {
  opacity: 0
}
.navbar-light .navbar-brand {
  margin-left: 15px;
  color: #2196f3 !important;
  font-weight: bolder;
}
</style>
