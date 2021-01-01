<template>
  <el-container class="m5 p-5" style="height: 90vh">
    <div class="d-flex h-100 w-100 align-items-center justify-content-center">
      <div class="shadow el-zoom-in-bottom p-5 rounded" style="background-color: #545c64">
        <p class="font-weight-light text-white" style="font-size: 2em">Login</p>
        <el-input
          class="mb-3"
          clearable
          v-model="login"
        ></el-input>
        <el-input
          class="mb-3"
          clearable
          v-model="password"
          type="password"
        ></el-input>
        <el-button
          class="w-100 mb-3"
          type="warning"
          @click="submit"
        >
          Submit
        </el-button>
      </div>
    </div>
  </el-container>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      login: 'admin',
      password: 'admin'
    }
  },
  methods: {
    submit () {
      if (this.login === this.password) {
        this.$cookie.set('username', this.login, '1D')
        this.$router.push('/')
      } else {
        this.$message({
          message: 'Oops! Invalid credentials :(',
          type: 'error'
        })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
