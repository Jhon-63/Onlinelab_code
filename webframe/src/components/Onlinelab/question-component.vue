<template>
  <Row class="mainTable">
    <!-- 大标题 -->
    <Divider size="small" v-if="module!='null'" orientation="left">{{module}}</Divider>
    <!-- 例：1.功能和实际用户应用场景适配度 -->
    <Row>
      <span style="font-size: 15px; font-weight: bold; color: rgb(70, 76, 91);">{{index+1}}.{{questionTitle}}</span>
    </Row>
    <!-- 例：评估软件实际项目交付定制工作量占比，得分=10*（1-定制%） -->
    <Row>
      <span style="font-size: 12px; color: rgb(158, 167, 180);">{{judgeCriteria}}</span>
    </Row>
    <!-- 得分 -->
    <Row>
      <Rate ref="ComA" clearable show-text allow-half :value="myvalue"  v-on:on-change="changeData">
          <span style="color: #f5a623">{{myvalue*2}}</span>
      </Rate>
    </Row>
  </Row>
</template>

<script>
export default {
  name: 'OlQuestion',
  props:{
    questionTitle: {
      type: String,
      default: () => ""
    },
    judgeCriteria: {
      type: String,
      default: () => ""
    },
    myvalue: {
      type:Number,
      default: ()=> 0
    },
    index: {
      type:Number,
      default: ()=> 0
    },
    module: {
      type: String,
      default: () => "null"
    },
    loadData: Function
  },
// 将评分更新数据传回父节点
  methods: {
    changeData(val){
      this.$emit('give-advice',{index:this.index,data:{module: this.module, title: this.questionTitle, judge: this.judgeCriteria, score: val}});
    }
  },
  data () {
    return {
      // module: "null"
    }
  },
}
</script>

<style>
  .mainTable{
    padding-left: 1rem;
  }
</style>
