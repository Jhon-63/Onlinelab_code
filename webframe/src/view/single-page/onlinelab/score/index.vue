<template>
    <div>
      <!-- 填写评分表格 -->
      <Card>
        <div class="baseInfo">
          <!-- 基本信息填写 -->
          <Divider size="small"orientation="left">基本信息</Divider>
          <Row>
            <span class="mySpan">公司名：</span><Input v-model="base_info.company_name" clearable  placeholder="华为技术有限公司" style="width: auto" />
          </Row>
          <Row>
            <span class="mySpan">解决方案名：</span><Input v-model="base_info.solution_name" clearable  placeholder="智慧停车解决方案" style="width: auto" />
          </Row>
          <Row>
            <span class="mySpan">行业类型：</span><Input v-model="base_info.business_type" clearable  placeholder="请用逗号隔开:如交通、物流" style="width: auto" />
            <span class="mySpan">业务类型：</span><Input v-model="base_info.industry_type" clearable  placeholder="请用逗号隔开:如监控、园区" style="width: auto" />
          </Row>
          <Row>
            <span class="mySpan">填写人：</span><Input v-model="base_info.user_name" clearable  placeholder="XX飞" style="width: auto" />
            <span class="mySpan">填写日期：</span><DatePicker v-model="base_info.time" class="datePicker" type="date" placeholder="选择填表日期" style="width: auto"></DatePicker>
          </Row>
        </div>

        <!-- 表格主体 -->
        <OlQuestion class="olQuestion" @give-advice="showAdvice" v-for="(question,index) in question_list" :judgeCriteria="question.judge"
        :questionTitle="question.title" :myvalue="question.score" :index="index" :module="question.module">
        </OlQuestion>

        <div>
          <strong>总得分：{{total_score}}</strong>

        </div>

        <Button class="submit" type=primary v-on:click="submit_table">提交评分表</Button>
        <Button class="submit" type=primary v-on:click="get_score_info">获取评分表信息</Button>

      </Card>

    </div>
</template>

<script>
import OlQuestion from '../../../../components/Onlinelab/question-component.vue'
import axios from 'axios';
import { postScoreTable,getScoreTable } from '@/api/data'


export default {
  components: {
    OlQuestion
  },
  computed: {
    total_score: function() {
      let count = 0;
      for(let i=0;i<this.question_list.length;i++)
      {
        count+=this.question_list[i].score*this.weight_table[i].weight;
      }
      return (count*2).toFixed(2);
    }

  },

  data () {
    return {
      question_list: [
        {module:"功能性",title: '功能和实际用户应用场景适配度', judge: '评估软件实际项目交付定制工作量占比，得分=10*（1-定制%）', score: 0},
        {title: '功能清单符合用户实际需要', judge: '有多少功能是用户用不上的，得分=10*（1-无用功能%）', score: 0},
        {title: '安全和隐私保护', judge: '扣分项：高危漏洞 2分/个，中危0.5分/个（5分封顶），低危0.1/个（2分封顶），A类红线2分/个；', score: 0},
        {module:"可靠性",title: '容灾、备份能力', judge: '前台应用占20%（集群10分；主备8分；单机5分）后台应用占30%（集群10分；主备8分；单机5分）；数据库（数据）容灾备份占50%（集群10分；主备8分；单机5分）；', score: 0},
        {module:"易用性",title: '操作简便易用', judge: '扣分项：一个业务场景超过6个操作步骤扣1分，超过10步骤以上扣2分；常用功能深度大于2的扣1分/个；关键操作输入没提示扣 0.1/个；其他扣分项0.1/个；', score: 0},
        {title: '学习上手快，自学习', judge: '有自向导或在线帮助文档，且指导文档易懂：8~10分；离线帮助文档，且指导文档易懂：7~8分；无帮助文档或操作指导：5~6分；', score: 0},
        {title: '关键操作、信息容易引起用户注意', judge: '主要应用场景的功能入口或操作是否醒目或容易找到（不符合扣1~2分）；错误提示告警是否醒目易懂（不符合扣0.5分~1分）；', score: 0},
        {module:"效率",title: '大量用户业务响应时间率', judge: '操作响应时间：CPU<70,内存<50正常负载范围的压测场景，平均响应时间<2S，>2S扣0.5分/个；最大相应时间大于5S的扣分 0.5/个；', score: 0},
        {title: '并发业务响应时间符合率', judge: '操作响应时间：CPU<70,内存<50正常负载范围的压测场景，平均响应时间<2S，>2S扣0.5分/个；最大相应时间大于5S的扣分 0.5/个；', score: 0},
        {title: '大量用户业务资源利用符合率', judge: 'CPU、内存、IO同规格支持并发等性能参数同行对比（先不关注评估）', score: 0},
        {title: '并发业务资源利用符合率', judge: 'CPU、内存、IO同规格支持并发等性能参数同行对比（先不关注评估）', score: 0},
        {module:"可维护性",title: '系统提供的数据规范、正确 ', judge: '有日志分析工具，日志在界面展示正确能帮助定位：9~10分;后台查看日志，日志信息格式规范、准确：8~9分；有日志信息但不规范或不准确：6~7分；缺或无日志信息：4~5分', score: 0},
        {title: '系统参数可修改性', judge: '常用配置参数可以通过界面配置（8~10分）；后台配置文件配置（7~8分）；缺少配置需要修改代码（5~6分）；配置是否需要重启生效，常用配置需要重启扣1分/个；', score: 0},
        {module:"可移植性",title: '兼容性', judge: '起评分5分，IE、Firefox、Chrome常用浏览器支持,多支持1种加1分；支持X86兼容ARM的加2分，夸1种操作系统加1分，最高分满分10分', score: 0},
        {title: '安装部署', judge: '全自动化部署，容器部署等小时级（4小时内）完成安装部署9~10分；自动+手动部署，或天级（小于2天内）完成部署，7~8分；全手动安装，安装部署大于2天，5~6分；', score: 0},
      ],
      weight_table:[
        {weight:0.12},{weight:0.09},{weight:0.09},{weight:0.1},{weight:0.1},{weight:0.06},{weight:0.04},{weight:0.025},
        {weight:0.025},{weight:0.025},{weight:0.025},{weight:0.06},{weight:0.14},{weight:0.05},{weight:0.05},
      ],
      base_info:{
        company_name:"",solution_name:"",business_type:"",industry_type:"",user_name:"",time:""
      }

    }
  },
  methods: {
    showAdvice(advice){
      // 更新评分值
      this.question_list.splice(advice.index,1,advice.data);
    },

    // 获取评分列表
    get_score_list(){
      var score_list_data = [];
      for(let i=0;i<this.question_list.length;i++)
      {
        let one_score_data = {index:i+1,score:this.question_list[i].score*2};
        score_list_data.push(one_score_data);
      };
      return {"score_list":score_list_data};
    },

    // 提交数据
    submit_table(){
      console.log("hello!");
      var score_list = JSON.stringify(this.get_score_list());
      var base_info = JSON.stringify(this.base_info);
      var return_data = (score_list+base_info).replace(/}{/, ',');

      console.log(return_data);

      postScoreTable(return_data).then(res => {
        console.log("success");
        console.log(res.data);

      }).catch(err => {
        console.log(err);

      })
    },
    
    // 获取评分表信息
    get_score_info(){
      getScoreTable().then(res => {
        console.log(res);

      }).catch(err => {
        console.log(err);

      })
    },

      // axios.post('http://localhost:8000/post_score_table',{
      //   firstName:'Fred'
      // })
      // // axios.get('https://www.bilibili.com')
      // .then(response => (this.info = response ))
      // .catch(function (error) {
      //   console.log("hello!");
      // });
    },


}
</script>

<style lang="less">
  .olQuestion{
    padding: 0.125rem;
    margin-left:0.125rem;
    }
  .baseInfo {
    margin: 0.625rem;
    .mySpan{
      display: inline-block;
      width: 5.5rem;
      height: 1.875rem;
      margin: 0.5rem;
      margin-left: 1rem;
      font-size: 14px;
      font-weight: bold;
      color: #515a6e;
    }
   }


</style>
