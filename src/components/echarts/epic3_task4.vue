<template>
  <div class="max-w-sm rounded overflow-hidden shadow-lg">
    <img
      src="../../assets/images/wordCloud.jpg"
      alt="Word Cloud"
      class="w-full cursor-pointer"
      @click="toggleImageZoom"
    >

    <!-- 修改后的放大图片部分 -->
    <div
      v-if="showZoomedImage"
      class="fixed inset-0 bg-white bg-opacity-50 flex justify-center items-center"
      @wheel="handleWheel"
    >
      <img
        src="../../assets/images/wordCloud.jpg"
        alt="Word Cloud"
        class="max-w-3xl max-h-screen"
        :style="{ transform: `scale(${zoomLevel})` }"
        @click.stop="toggleImageZoom"
      >
    </div>

    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">词云分析</div>
      <p class="text-gray-700 text-base">
        这是从评论中生成的词云分析结果。
      </p>
    </div>
    <div class="px-6 pt-4 pb-2">
      <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#词云</span>
      <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#数据可视化</span>
      <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#评论分析</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showZoomedImage: false,
      zoomLevel: 1, // 初始缩放级别
    };
  },
  methods: {
    toggleImageZoom() {
      this.showZoomedImage = !this.showZoomedImage;
    },
    handleWheel(event) {
      event.preventDefault(); // 阻止默认滚动行为
      const zoomChange = event.deltaY * -0.001; // 根据滚轮方向调整缩放变化量
      this.zoomLevel = Math.min(Math.max(0.5, this.zoomLevel + zoomChange), 1.6); // 限制缩放级别在0.5到5之间
    },
  },
};
</script>

  <style scoped>
/* 这里你可以添加一些额外的CSS样式，如果需要的话 */
.cursor-pointer {
  cursor: pointer;
}
</style>
