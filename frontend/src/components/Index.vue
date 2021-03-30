<template>
  <div class="container">
    <p class="font-weight-lighter mb-1" style="font-size: 3rem">Welcome</p>
    <p class="font-weight-lighter" style="font-size: 1.5rem">
      Handyman is simple event-driven application powered by Python & Vue.js
    </p>
    <hr>
    <div class="text-left">
      <p class="mb-2" style="font-size: 1.2rem">Sitemap:</p>
      <p class="font-weight-lighter" style="font-size: 1.2rem">
        1) <router-link to="/storage" class="m-0 p-0">Storage</router-link> - upload / download your files via websockets.
      </p>
      <p class="font-weight-lighter" style="font-size: 1.2rem">
        2) <router-link to="/dummy" class="m-0 p-0">Dummy</router-link> - let's create background tasks in Celery!
        By default a main function of every worker is reversing a string (the name of task) for some period of time,
        provided by user. For example, if the name of the task is "TASK-1", you'll get "1-KSAT" as a result. Try it.
      </p>
    </div>
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
