<template>
  <div>
    <TopmenuVue
      :menu-items="menuItems"
      :content-components="contentComponents"
    />
  </div>
</template>

<script>
import exampleVue from '@comp/echarts/example.vue';
import TopmenuVue from '../../components/basic/Topmenu.vue';

export default {
  components: {
    TopmenuVue,
  },
  data() {
    return {
      menuItems: [
        {
          title: '图表',
          key: 'chart',
          children: [
            { title: 'ECharts图表', key: 'echarts' },
          ],
        },
        {
          title: '自定义',
          key: 'custom',
          children: [
            { title: '自定义组件', key: 'customComp' },
          ],
        },
      ],
    };
  },
  computed: {
    contentComponents() {
      return {
        echarts: exampleVue, // 直接引用组件对象
        customComp: exampleVue,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
