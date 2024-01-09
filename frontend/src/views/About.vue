<template>
  <div id="about">
    <el-form :model="ruleForm" status-icon :rules="rules" ref="addScheduleForm" label-width="120px" class="addScheduleForm">
      <div style="margin: 10px; padding: 10px; border: solid 1px rgb(150, 138, 189);">
        <h1>グーグルカレンダー</h1>
        <h3>・予定を追加</h3>
        <el-form-item class="addSchedule-block">
          <div>
              <span>予定のタイトル入力欄</span>
              <el-input
                type="textarea"
                :autosize="{ minRows: 1, maxRows: 4 }"
                placeholder="ここに入力できます。"
                v-model="addScheduleForm.title_text">
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
              v-model="addScheduleForm.description_text">
            </el-input>
          </div>
        </el-form-item>
          
        <el-form-item class="addSchedule-block">
          <div class="block">
            <span style="margin-right: 20px;">日時期間</span>
            <el-date-picker
              v-model="addScheduleForm.dayValues"
              type="datetimerange"
              range-separator="～"
              start-placeholder="開始"
              end-placeholder="終了"
              align="right"
              :default-time="['00:00:00', '23:59:59']">
            </el-date-picker>
          </div>
        </el-form-item>
        <el-form-item class="addSchedule-block">
          <el-row>
            <el-button @click="submitForm" type="success" plain>追加</el-button>
            <el-button @click="resetForm" type="danger" plain>リセット</el-button>
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
    var validate = function(rule, value, callback) {
      if (value === '') {
        callback(new Error('入力してください。'));
      } else {
        callback();
      }
    };
    return {
      tableData: [],
      addScheduleForm: {
        title_text: '',
        description_text: '',
        dayValues: ''
      },
      rules: {
        title_text: [
          { validator: validate, trigger: 'blur' }
        ],
        description_text: [
          { validator: validate, trigger: 'blur' }
        ],
        dayValues: [
          { validator: validate, trigger: 'blur' }
        ]
      }
    }
  },
  mounted() {
    
  },
  methods: {
    submitForm: async function() {
      console.log(this.addScheduleForm)
      // print(this.axios)
      var params = new FormData()
      params.append("title_text", this.addScheduleForm.title_text)
      params.append("description_text", this.addScheduleForm.description_text)
      params.append("start_date", [this.addScheduleForm.dayValues[0].getFullYear(), this.addScheduleForm.dayValues[0].getMonth() + 1, this.addScheduleForm.dayValues[0].getDate(), this.addScheduleForm.dayValues[0].getHours(), this.addScheduleForm.dayValues[0].getMinutes(), this.addScheduleForm.dayValues[0].getSeconds()] )
      params.append("end_date", [this.addScheduleForm.dayValues[1].getFullYear(), this.addScheduleForm.dayValues[1].getMonth() + 1, this.addScheduleForm.dayValues[1].getDate(), this.addScheduleForm.dayValues[1].getHours(), this.addScheduleForm.dayValues[1].getMinutes(), this.addScheduleForm.dayValues[1].getSeconds()])
      axios.post('/scadule/add', params)
        .then(function (response) {
          console.log('Create axios response')
          console.log(response)
        })
        .catch(err => {
          console.log('Create axios error')
          console.log(err)
        })

    },
    resetForm: async function () {
      this.addScheduleForm.title_text = '';
      this.addScheduleForm.description_text = '';
      this.addScheduleForm.dayValues = '';
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