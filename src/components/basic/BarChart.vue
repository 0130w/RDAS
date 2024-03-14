<template>
  <TopmenuVue
    :menu-items="menuItems"
    :content-components="contentComponents"
  />
</template>

<script>
import epic1_task1 from '@comp/echarts/epic1_task1.vue';
import epic1_task2 from '@comp/echarts/epic1_task2.vue';
import epic1_task3 from '@comp/echarts/epic1_task3.vue';
import epic1_task4 from '@comp/echarts/epic1_task4.vue';
import epic1_task5 from '@comp/echarts/epic1_task5.vue';
import epic1_task7 from '@comp/echarts/epic1_task7.vue';
import epic1_task8 from '@comp/echarts/epic1_task8.vue';
import epic1_task9 from '@comp/echarts/epic1_task9.vue';
import epic1_task10 from '@comp/echarts/epic1_task10.vue';
import epic1_task11 from '@comp/echarts/epic1_task11.vue';
import epic1_task12 from '@comp/echarts/epic1_task12.vue';
import epic2_task1 from '@comp/echarts/epic2_task1.vue';
import epic2_task2 from '@comp/echarts/epic2_task2.vue';
import epic2_task3 from '@comp/echarts/epic2_task3.vue';
import epic2_task4 from '@comp/echarts/epic2_task4.vue';
import epic2_task5 from '@comp/echarts/epic2_task5.vue';
import epic2_task6_checkin from '@comp/echarts/epic2_task6_checkin.vue';
import epic2_task6_elite from '@comp/echarts/epic2_task6_elite.vue';
import epic2_task6_review from '@comp/echarts/epic2_task6_review.vue';
import epic2_task6_tips from '@comp/echarts/epic2_task6_tips.vue';
import TopmenuVue from './Topmenu.vue';

export default {
  components: {
    TopmenuVue,
    epic1_task1,
    epic1_task2,
    epic1_task3,
    epic1_task4,
    epic1_task5,
    epic1_task7,
    epic1_task8,
    epic1_task9,
    epic1_task10,
    epic1_task11,
    epic1_task12,
    epic2_task1,
    epic2_task2,
    epic2_task3,
    epic2_task4,
    epic2_task5,
    epic2_task6_checkin,
    epic2_task6_elite,
    epic2_task6_review,
    epic2_task6_tips,
  },
  data() {
    return {
      menuItems: [
        {
          title: '商户视角',
          key: 'bussiness',
          children: [
            { title: '找出美国最常见商户（前20）', key: 'e1t1' },
            { title: '找出美国商户最多的前10个城市', key: 'e1t2' },
            { title: '找出美国商户最多的前5个州', key: 'e1t3' },
            { title: '找出美国最常见商户，并显示平均评分（前20）', key: 'e1t4' },
            { title: '统计评分最高的城市（前10）', key: 'e1t5' },
            { title: '统计最多的category及数量（前10）', key: 'e1t7' },
            { title: '收获五星评论最多的商户（前20）', key: 'e1t8' },
            { title: '统计不同类型（中国菜、美式、墨西哥）的餐厅的评论数量', key: 'e1t10' },
            { title: '统计不同类型（中国菜、美式、墨西哥）的餐厅的评分分布', key: 'e1t11' },
          ],
        },
        {
          title: '用户视角',
          key: 'user',
          children: [
            { title: '分析每年加入的用户数量', key: 'e2t1' },
            { title: '统计评论达人', key: 'e2t2' },
            { title: '统计人气最高的用户', key: 'e2t3' },
            { title: '统计每年优质用户、普通用户比例', key: 'e2t4' },
            { title: '显示每年总用户数、沉默用户数的比例', key: 'e2t5' },
            { title: '统计出每年的打卡用户数', key: 'e2t6_checkin' },
            { title: '统计出每年的精英用户数', key: 'e2t6_elite' },
            { title: '统计出每年的评论数', key: 'e2t6_review' },
            { title: '统计出每年的tips数', key: 'e2t6_tips' },
          ],
        },
      ],
    };
  },
  computed: {
    contentComponents() {
      return {
        e1t1: epic1_task1, // 直接引用组件对象
        e1t2: epic1_task2,
        e1t3: epic1_task3,
        e1t4: epic1_task4,
        e1t5: epic1_task5,
        e1t7: epic1_task7,
        e1t8: epic1_task8,
        e1t10: epic1_task10,
        e1t11: epic1_task11,
        e2t1: epic2_task1,
        e2t2: epic2_task2,
        e2t3: epic2_task3,
        e2t4: epic2_task4,
        e2t5: epic2_task5,
        e2t6_checkin: epic2_task6_checkin,
        e2t6_elite: epic2_task6_elite,
        e2t6_review: epic2_task6_review,
        e2t6_tips: epic2_task6_tips,
      };
    },
  },
};
</script>

<style>
</style>
