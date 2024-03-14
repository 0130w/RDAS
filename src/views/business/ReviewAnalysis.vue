<template>
  <div class="w-full">
    <h1 class="text-2xl font-bold text-center">评论系统</h1>
    <div class="flex">
      <!-- 左侧内容 -->
      <div class="w-4/7 h-full p-2 rounded-lg">
        <epic3_task2 />
      </div>
      <!-- 右侧内容 -->
      <div class="w-3/7 h-full p-2 rounded-lg">
        <epic3_task1 />
      </div>
    </div>
    <div class="flex">
      <!-- 左侧内容 -->
      <div class="w-4/7 h-full p-2 rounded-lg">
        <epic3_task3 />
      </div>
      <!-- 右侧内容 -->
      <div class="w-3/7 h-full p-2 rounded-lg">
        <epic3_task4 />
      </div>
    </div>
  </div>

</template>

<script>
import epic3_task1 from '@comp/echarts/epic3_task1.vue';
import epic3_task2 from '@comp/echarts/epic3_task2.vue';
import epic3_task3 from '@comp/echarts/epic3_task3.vue';
import epic3_task4 from '@comp/echarts/epic3_task4.vue';

export default {
  components: {
    epic3_task1, epic3_task2, epic3_task3, epic3_task4,
  },
};
</script>

<style>
</style>
