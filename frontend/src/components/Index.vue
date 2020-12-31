<template>
  <div class="container">
    <p class="font-weight-lighter mb-1" style="font-size: 3rem">Welcome</p>
    <p class="font-weight-lighter" style="font-size: 1.5rem">
      Handyman is simple event-driven application powered by Python & Vue.js
    </p>
    <p class="font-weight-lighter" style="font-size: 1.2rem">
      Let's navigate to <router-link to="/tasks" class="m-0 p-0">tasks</router-link> and create some work for Celery :)
    </p>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
