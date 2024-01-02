<template>
  <div id="about">
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="120px" class="addScheduleForm">
      <div style="margin: 10px; padding: 10px; border: solid 1px rgb(150, 138, 189);">
        <el-form-item class="addSchedule-block">
          <div>
              <span>予定のタイトル入力欄</span>
              <el-input
                type="textarea"
                :autosize="{ minRows: 1, maxRows: 4 }"
                placeholder="ここに入力できます。"
                v-model="title_text">
              </el-input>
          </div>
        </el-form-item>
          
        <el-form-item class="addSchedule-block">
          <div class="block">
            <span>備考</span>
            <el-input
              type="textarea"
              :autosize="{ minRows: 2, maxRows: 4 }"
              placeholder="ここに入力できます。"
              v-model="description_text">
            </el-input>
          </div>
        </el-form-item>
          
        <el-form-item class="addSchedule-block">
          <div class="block">
            <span style="margin-right: 20px;">日時期間</span>
            <el-date-picker
              v-model="dayValues"
              type="datetimerange"
              range-separator="～"
              start-placeholder="開始"
              end-placeholder="終了"
              align="right"
              :default-time="['00:00:00', '23:59:59']">
            </el-date-picker>
          </div>
        </el-form-item>
          {{ dayValues[0] }}
        <el-form-item class="addSchedule-block">
          <el-row>
            <el-button type="primary" plain>追加</el-button>
            <el-button type="danger" plain>リセット</el-button>
          </el-row>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'about-test',
  data() {
    return {
      tableData: [],
      dayValues: '',
      description_text: '',
      title_text: '',
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
.addScheduleForm {
  width: 800px;
}

</style>
<style>
.addSchedule-block .el-form-item__content{
  margin: 0 !important;
}
</style>