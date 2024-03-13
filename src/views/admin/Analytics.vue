<template>
  <div>
    <searchView />
    <!-- 使用 exampleVue 组件 -->
    <exampleVue></exampleVue>
  </div>
</template>

<script>
import searchView from '@comp/basic/search.vue';
import exampleVue from '@comp/echarts/example.vue';

export default {
  components: {
    exampleVue, searchView,
  },
};
</script>

<style lang="scss" scoped>
</style>
