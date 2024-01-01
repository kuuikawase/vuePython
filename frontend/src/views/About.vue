<template>
  <div class="about">
    <h1>クリックして、音楽を再生してください。</h1>
    <el-table class="data-table" :data="tableData" stripe>
      <el-table-column prop="id" label="ID" width="180"></el-table-column>
      <el-table-column prop="name" label="名前" width="180"></el-table-column>
      <el-table-column prop="path" label="Path"></el-table-column>
    </el-table>
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'about-test',
  data() {
    return {
      tableData: []
    }
  },
  mounted() {
    this.updataTableData()
  },
  methods: {
    updataTableData: async function () {
      const response = await axios.get('/music/location')
      this.tableData = response.data
    }
  }
}
</script>

<style scoped>
.data-table {
  width: 80%;
  margin: auto;
}
</style>
