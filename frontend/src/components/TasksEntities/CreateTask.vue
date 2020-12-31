<template>
  <div>
    <el-button type="warning" @click="dialogVisible = true" class="text-dark">Create</el-button>

    <el-dialog
      :visible.sync="dialogVisible"
      width="40%"
      :show-close="false"
      :before-close="handleClose">
      <h5 class="h5 mt-0 pt-0">Create new background task</h5>
      <el-divider class="mt-0 pt-0"></el-divider>
      <div class="p-4">
        <el-input
          placeholder="Task description"
          v-model="form.description"
          class="mb-2"
          clearable>
        </el-input>
        <el-select class="w-100 mb-2" v-model="form.time" placeholder="Work for ...">
          <el-option
            v-for="(item, index) in [10, 20, 30, 60, 120, 240, 360]"
            :key="'select__yb'+index"
            :label="item + ' seconds'"
            :value="item">
          </el-option>
        </el-select>
        <el-select class="w-100" v-model="form.priority" placeholder="Select priority">
          <el-option
            v-for="(item, index) in ['low', 'medium', 'high']"
            :key="'select__prior'+index"
            :label="item"
            :value="item">
          </el-option>
        </el-select>
      </div>
      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submit">Confirm</el-button>
  </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CreateTask',
  data () {
    return {
      dialogVisible: false,
      form: {
        description: '',
        time: 'Work for...',
        priority: 'Select priority (not working for now)',
        username: 'admin'
      }
    }
  },
  methods: {
    handleClose (done) {
      done()
    },
    submit () {
      this.$socket.emit('create_task', this.form)
      this.form.description = ''
      this.form.time = 'Work for...'
      this.form.priority = 'Select priority'
      this.dialogVisible = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.el-dialog__body {
  padding: 0 !important;
}

.el-dialog__header {
  padding: 8px !important;
}

</style>
