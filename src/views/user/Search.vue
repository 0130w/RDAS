<template>
  <div class="flex">
    <!-- 左侧内容 -->
    <div class="w-2/5 h-full p-4">
      <!-- 这里放置左侧的内容 -->
      <div class="bg-gray-100 h-full p-4 rounded-lg">
        <SearchBox />
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="w-3/5 p-5">
      <!-- 这里放置右侧的内容 -->
      <div class="bg-gray-200 h-full p-4 rounded-lg">
        Right Content
      </div>
    </div>
  </div>

</template>

<script>
import SearchBox from '@comp/basic/SearchBox.vue';

export default {
  components: {
    SearchBox,
  },
};
</script>

<style>
</style>
