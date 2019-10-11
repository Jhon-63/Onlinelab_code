<template>
  <div>
    <Table :columns="columns" :data="tabeldata"></Table>
  </div>

</template>

        single_data = {'company_name': single_score.company_name, 'solution_name':  single_score.solution_name,
                         'business_type': single_score.business_type, 'industry_type': single_score.industry_type,
                         'user_name': single_score.judges, 'time': single_score.date}

<script>
import { getScoreTable } from '@/api/data'


export default {
        data () {
            return {
                columns: [
                    {
                        title: '解决方案名',
                        key: 'solution_name'
                    },
                    {
                        title: '公司名称',
                        key: 'company_name'
                    },
                    {
                        title: '业务类型',
                        key: 'business_type'
                    },
                    {
                        title: '行业类型',
                        key: 'industry_type'
                    },
                    {
                        title: '打分人',
                        key: 'user_name'
                    },
                    {
                        title: '填表日期',
                        key: 'time'
                    },
                    {
                        title: '总得分',
                        key: 'total_score',
                        sortable: true
                    }
                ],
                tabeldata: []
            }
        },
        mounted() {
            getScoreTable().then(res => {
              console.log(res);
              console.log("------------");
              const data = [];
              var score_list = res.data;
              for (let i = 0;i< score_list.length;i++)
              {
                console.log(score_list[i]);
                this.tabeldata.push(score_list[i]);

              }


            }).catch(err => {
              console.log(err);

            })


        }


    }

</script>

<style>




</style>
