<template>
  <div class="container">
    <p class="font-weight-lighter mb-1" style="font-size: 3rem">Welcome</p>
    <p class="font-weight-lighter" style="font-size: 1.5rem">
      This is simple event-driven application powered by Python FastAPI & Vue.js
    </p>
    <p class="font-weight-lighter" style="font-size: 1.2rem">
      Choose your test case to see how it works: try to create tasks or go to chat and write some text to other people
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
