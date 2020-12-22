<template>
  <el-col :span="6" class="p-2">
    <el-card shadow="hover" class="p-0">
      <div class="d-flex justify-content-between align-items-center">
        <p class="m-0 p-0 text-left" style="font-size: 1.2rem">Task # {{ data.task_id }} </p>
        <div>
          <span class="m-0 p-0" style="font-size: 0.9rem; line-height: 1.1"><i class="el-icon-finished"></i> Priority:</span>
          <el-tag v-if="data.priority === 'medium'" type="warning">{{ data.priority }}</el-tag>
          <el-tag v-if="data.priority === 'low'" type="success">{{ data.priority }}</el-tag>
          <el-tag v-if="data.priority === 'high'" type="danger">{{ data.priority }}</el-tag>
        </div>
      </div>
      <el-divider class="my-2"></el-divider>
      <el-row :gutter="24">
        <el-col :span="8">
          <el-progress type="dashboard" :percentage="data.percent" :color="colors"></el-progress>
        </el-col>
        <el-col :span="16" class="text-left pl-5 py-2">

          <p class="m-0 p-0" style="font-size: 0.9rem; line-height: 1.1"><b><i class="el-icon-edit"></i> Description:</b></p>
          <p class="m-0 p-0 mb-2" style="font-size: 0.9rem; line-height: 1.1">{{ data.description }}</p>

          <p class="m-0 p-0" style="font-size: 0.9rem; line-height: 1.1"><b><i class="el-icon-user-solid"></i> Owner:</b></p>
          <p class="m-0 p-0 mb-2" style="font-size: 0.9rem; line-height: 1.1">{{ data.username }}</p>

        </el-col>
      </el-row>
    </el-card>
  </el-col>
</template>

<script>
export default {
  name: 'Task',
  props: {
    data: Object
  },
  data () {
    return {
      colors: [
        {color: '#f56c6c', percentage: 30},
        {color: '#e6a23c', percentage: 70},
        {color: '#5cb87a', percentage: 100}
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.el-card__body {
  padding: 0.7rem !important;
}

</style>
