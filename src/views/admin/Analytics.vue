<template>
  <div>

    <!-- 使用 exampleVue 组件 -->
    <epic1_task2></epic1_task2>

  </div>
</template>

<script>
import searchView from '@comp/basic/search.vue';
import exampleVue from '@comp/echarts/example.vue';
import epic1_task2 from '@comp/echarts/epic1_task5.vue';

export default {
  components: {
    exampleVue, epic1_task2,
  },
};
</script>

<style lang="scss" scoped>
</style>
