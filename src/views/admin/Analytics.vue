<template>
  <div class="flex">
    <!-- 左侧内容 -->
    <div class="w-3/5 h-full p-4">
      <!-- 这里放置左侧的内容 -->
      <div class="bg-gray-100 h-full p-4 rounded-lg">
        <h1 class="text-2xl font-bold text-center mb-6">您的商户画像</h1>
        <TopmenuVue
          :menu-items="menuItems"
          :content-components="contentComponents"
        />
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="w-2/5 p-5">
      <!-- 这里放置右侧的内容 -->
      <div class="bg-gray-200 h-full p-4 rounded-lg">

      </div>
    </div>
  </div>

</template>

<script>
import exampleVue from '@comp/echarts/example.vue';
import epic1_task12 from '@comp/echarts/epic1_task12.vue';
import epic2_task1 from '@comp/echarts/epic2_task1.vue';
import TopmenuVue from '../../components/basic/Topmenu.vue';

export default {
  // Code block with the fix
  components: {
    TopmenuVue, epic2_task1,
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
        echarts: epic2_task1, // 直接引用组件对象
        customComp: exampleVue,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
