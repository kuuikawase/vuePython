<template>
  <div class="home">
    <h1>クリックで音楽を再生します。</h1>

    <el-row class="grid_row" :gutter="12" v-for="(tableData, index) in grouped_array" :key="index">
      <el-col :span="8" v-for="data in tableData" :key="data.id">
        <a @click="{{ playMusic(data.path, data.musicname) }}">
        <el-card shadow="hover">
            {{ data.musicname }}
        </el-card>
        </a>
      </el-col>
    </el-row>
  </div>
</template>

<script>
const axios = require('axios').create()

export default {
  name: 'home-test',
  data () {
    return {
      tableData : [],
      grouped_array: []
    }
  },
  mounted () {
    this.updataTableData()
  }, 
  computed: {
    form() {
      return {
        name: this.name,
        path: this.path
      }
    }
  },
  methods: {
    updataTableData: async function () {
      const response = await axios.get('/music/location')
      this.tableData = response.data
      // 一行ごとに分割
      const split_count = 3
      const count = this.tableData.length
      for (let i = 0; i < Math.ceil(count / split_count); i++) {
        let multiple_count = i * split_count
        let result = this.tableData.slice(multiple_count, multiple_count + split_count)
        this.grouped_array.push(result)
      }
    },
    playMusic : async function (path, name) {
      console.log(name)
      // print(this.axios)
      var params = new FormData()
      params.append("path", path)
      params.append("name", name)
      axios.post('/music/play', params)
      .then(function (response) {
        console.log('Create axios response')
        console.log(response)
      })
        .catch(err => {
          console.log('Create axios error')
          console.log(err)
        })

    }
  }
}
</script>

<style scoped>
.grid_row {
  margin-bottom: 10px;
}
.data-table {
  width: 80%;
  margin: auto;
}
a, a:hover, a:visited {
  color:black;
  text-decoration: none;
}
</style>
