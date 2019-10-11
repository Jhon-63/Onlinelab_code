<template>
    <div>
        <!-- <Row>
            <Steps :current="1">
                <Step title="已完成" content="选择方案"></Step>
                <Step title="进行中" content="点击检查组件"></Step>
                <Step title="待进行" content="修改确认"></Step>
                <Step title="待进行" content="保存至数据库"></Step>
            </Steps>
        </Row> -->


        <Row>
            <!-- 主界面 -->
            <Col span="18">界面
                <Row>
                    <Select v-model="model1" style="width:400px">
                        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </Row>
                <Row>
                    <Divider orientation="left">业务类型</Divider>                    
                    <Row>
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />                                         
                    </Row>
                    <Divider orientation="left">行业属性</Divider>                    
                    <Row>
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />
                        <Input v-model="value" placeholder="Enter something..." style="width: 300px" />                        
                        
                    </Row>         
                    <Divider orientation="left">组件信息</Divider>                         
                    <Row>
                        <Table stripe border :columns="columns1" :data="data1"></Table>
  
                    </Row>
                    <Row >
                        <Button type="primary">检验</Button>
                        <Button type="primary">保存至数据库</Button>
                    </Row>

                </Row>
            </Col>
            <!-- 组件信息 -->
            <Col span="6">组件信息
                <Collapse simple v-model="value1">
                    <Panel name="1">
                        史蒂夫·乔布斯
                        <p slot="content">史蒂夫·乔布斯（Steve Jobs），1955年2月24日生于美国加利福尼亚州旧金山，美国发明家、企业家、美国苹果公司联合创办人。</p>
                    </Panel>
                    <Panel name="2">
                        斯蒂夫·盖瑞·沃兹尼亚克
                        <p slot="content">斯蒂夫·盖瑞·沃兹尼亚克（Stephen Gary Wozniak），美国电脑工程师，曾与史蒂夫·乔布斯合伙创立苹果电脑（今之苹果公司）。斯蒂夫·盖瑞·沃兹尼亚克曾就读于美国科罗拉多大学，后转学入美国著名高等学府加州大学伯克利分校（UC Berkeley）并获得电机工程及计算机（EECS）本科学位（1987年）。</p>
                    </Panel>
                    <Panel name="3">
                        乔纳森·伊夫
                        <p slot="content">乔纳森·伊夫是一位工业设计师，现任Apple公司设计师兼资深副总裁，英国爵士。他曾参与设计了iPod，iMac，iPhone，iPad等众多苹果产品。除了乔布斯，他是对苹果那些著名的产品最有影响力的人。</p>
                    </Panel>
                </Collapse>            
            </Col>

        </Row>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                cityList: [
                    {
                        value: 'New York',
                        label: 'New York'
                    },
                    {
                        value: 'London',
                        label: 'London'
                    }
                ],
                model1: '',
                columns1: [
                    {
                        title: '组件名',
                        key: 'name'
                    },
                    {
                        title: '版本',
                        key: 'version'
                    },
                    {
                        title: '类型',
                        key: 'type'
                    }
                ],
                data1: [
                    {
                        name: 'John Brown',
                        version: 18,
                        type: 'New York No. 1 Lake Park',
                        date: '2016-10-03'
                    },
                    {
                        name: 'John Brown',
                        version: 18,
                        type: 'New York No. 1 Lake Park',
                        date: '2016-10-03'
                    },
                    {
                        name: 'John Brown',
                        version: 18,
                        type: 'New York No. 1 Lake Park',
                        date: '2016-10-03'
                    },
                    {
                        name: 'John Brown',
                        version: 18,
                        type: 'New York No. 1 Lake Park',
                        date: '2016-10-03'
                    },

                ]

            }
        }
    }
</script>