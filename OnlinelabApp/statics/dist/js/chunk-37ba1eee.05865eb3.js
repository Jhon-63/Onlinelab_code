(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-37ba1eee"],{"9be8":function(e,t,n){},b5bc:function(e,t,n){"use strict";var a=n("9be8"),o=n.n(a);o.a},f73e:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("Row",[n("i-col",[n("Card",[n("Row",[n("i-col",{attrs:{span:"8"}},[n("Button",{attrs:{type:"primary"},on:{click:e.showModal}},[e._v("显示可拖动弹窗")]),n("br"),n("Button",{directives:[{name:"draggable",rawName:"v-draggable",value:e.buttonOptions,expression:"buttonOptions"}],staticClass:"draggable-btn"},[e._v("这个按钮也是可以拖动的")])],1),n("i-col",{attrs:{span:"16"}},[n("div",{staticClass:"intro-con"},[e._v('\n              <Modal v-draggable="options" v-model="visible">标题</Modal>\n              '),n("pre",{staticClass:"code-con"},[e._v("  options = {\n    trigger: '.ivu-modal-body',\n    body: '.ivu-modal'\n  }\n              ")])])])],1)],1)],1),n("Modal",{directives:[{name:"draggable",rawName:"v-draggable",value:e.options,expression:"options"}],model:{value:e.modalVisible,callback:function(t){e.modalVisible=t},expression:"modalVisible"}},[e._v("\n      拖动这里即可拖动整个弹窗\n    ")])],1),n("Row",{staticStyle:{"margin-top":"10px"}},[n("i-col",[n("Card",[n("Row",[n("i-col",{attrs:{span:"8"}},[n("Input",{staticStyle:{width:"60%"},model:{value:e.inputValue,callback:function(t){e.inputValue=t},expression:"inputValue"}},[n("Button",{directives:[{name:"clipboard",rawName:"v-clipboard",value:e.clipOptions,expression:"clipOptions"}],attrs:{slot:"append"},slot:"append"},[e._v("copy")])],1)],1),n("i-col",{attrs:{span:"16"}},[n("div",{staticClass:"intro-con"},[e._v('\n              <Input style="width: 60%" v-model="inputValue">\n                '),n("br"),e._v('\n                   <Button slot="append" v-clipboard="clipOptions">copy</Button>\n                '),n("br"),e._v("\n              </Input>\n              "),n("pre",{staticClass:"code-con"},[e._v("  clipOptions: {\n    value: this.inputValue,\n    success: (e) => {\n      this.$Message.success('复制成功')\n    },\n    error: () => {\n      this.$Message.error('复制失败')\n    }\n  }\n              ")])])])],1)],1)],1),n("Modal",{directives:[{name:"draggable",rawName:"v-draggable",value:e.options,expression:"options"}],model:{value:e.modalVisible,callback:function(t){e.modalVisible=t},expression:"modalVisible"}},[e._v("\n      拖动这里即可拖动整个弹窗\n    ")])],1)],1)},o=[],i={name:"directive_page",data:function(){return{modalVisible:!1,options:{trigger:".ivu-modal-body",body:".ivu-modal",recover:!0},buttonOptions:{trigger:".draggable-btn",body:".draggable-btn"},statu:1,inputValue:"这是输入的内容"}},computed:{clipOptions:function(){var e=this;return{value:this.inputValue,success:function(t){e.$Message.success("复制成功")},error:function(){e.$Message.error("复制失败")}}}},methods:{showModal:function(){this.modalVisible=!0}}},s=i,l=(n("b5bc"),n("2877")),r=Object(l["a"])(s,a,o,!1,null,null,null);t["default"]=r.exports}}]);