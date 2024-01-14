<template>
  <div id="app">
    <el-menu :default-active="activeIndex" mode="horizontal" router>
      <el-menu-item index="home" :route="{ name:'home' }">Music</el-menu-item>
      <el-menu-item index="about" :route="{ name:'about' }">Calendarテスト</el-menu-item>
      <el-menu-item>
        <a href="https://element.eleme.io" target="_blank">UI_Link</a>
      </el-menu-item>
      <el-menu-item>
        <el-button v-on:click="stopMusic()" type="danger" plain>停止</el-button>
      </el-menu-item>
    </el-menu>
    <router-view />
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'app',
  data () {
    return {
      activeIndex: this.$route.name
    }
  },
  methods: {
    stopMusic: async function () {
      console.log("test")
      axios.post('/music/stop')
      .then(function (response) {
        console.log('Create axios response')
        console.log(response)
      })
      .catch(err => {
        console.log('Create axios error')
        console.log(err)
      })

    },
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
</style>
