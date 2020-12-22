<template>
  <div class="container">
    <p class="font-weight-lighter mb-1" style="font-size: 3rem">Welcome</p>
    <p class="font-weight-lighter" style="font-size: 1.5rem">
      This is simple event-driven application powered by Python FastAPI & Vue.js
    </p>
    <p class="font-weight-lighter" style="font-size: 1.2rem">
      Choose your test case to see how it works: try to create tasks or go to chat and write some text to other people
    </p>
    <p>Websockets Messages: {{ messages }}</p>
    <el-input label="Hello" v-model="input"></el-input>
    <el-button @click="submit">Send</el-button>
  </div>
</template>

<script>
export default {
  name: 'Tasks',
  data () {
    return {
      messages: [],
      input: 'Type Here'
    }
  },
  methods: {
    submit () {
      this.$socket.emit('custom_message', this.input)
    }
  },
  sockets: {
    custom_message (data) {
      this.messages.push(data)
    }
  },
  mounted () {
    this.$socket.connect()
    this.$socket.emit('custom_message', {hello: 'world'})
  },
  beforeRouteLeave (to, from, next) {
    this.$socket.disconnect()
    next()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
