<template>
  <div class="container-fluid">
    <div class="container-fluid d-flex justify-content-between align-items-center">

      <h2 class="font-weight-lighter mb-0">Background tasks</h2>

      <div class="d-flex">

        <el-button type="primary" class="mb-2" @click="emitTest">
          <span class="text-dark">Emit test</span>
        </el-button>

        <el-button type="info" class="mb-2" @click="delToken">
          <span class="text-dark">Filter</span>
        </el-button>

        <CreateTask class="ml-2"/>

      </div>

    </div>

    <el-divider class="bg-dark mt-1"></el-divider>

    <el-row>
      <Task v-for="(task, index) in tasks" :key="'task__n'+index" :data="task"/>
    </el-row>
  </div>
</template>

<script>
import Task from './TasksEntities/Task'
import CreateTask from './TasksEntities/CreateTask'

export default {
  name: 'Tasks',
  components: {
    Task,
    CreateTask
  },
  data () {
    return {
      tasks: [],
      input: 'Type Here'
    }
  },
  methods: {
    update () {
      this.$socket.emit('get_result', {username: 'admin'})
    },
    delToken () {
      this.$cookie.delete('username')
      this.$router.push({ name: 'Login' })
    },
    emitTest () {
      this.$socket.emit('test', {test: 'test'})
    }
  },
  sockets: {
    get_result (data) {
      this.tasks = data
    },
    create_task (data) {
      this.tasks.push(data)
    },
    worker_message (data) {
      for (let item of this.tasks) {
        if (item.task_id === data.task_id) {
          item.percent = parseInt(data.percent)
          if (item.percent > 99) {
            const index = this.tasks.indexOf(item)
            this.tasks.splice(index, 1)
            this.tasks.push(data)
          }
        }
      }
    },
    test (data) {
      this.$message.success(data.test)
    }
  },
  mounted () {
    this.$socket.emit('get_result', {username: 'admin'})
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
