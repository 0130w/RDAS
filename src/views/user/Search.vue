<template>
  <div class="flex">
    <!-- 左侧内容 -->
    <div class="w-4/7 h-full p-4">
      <!-- 这里放置左侧的内容 -->
      <div class="bg-gray-100 h-full p-4 rounded-lg">
        <SearchBox />
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="w-3/7 p-5">
      <!-- 这里放置右侧的内容 -->
      <div class="bg-gray-100 h-full p-4 rounded-lg">
        <BusinessCard :business="businessInfo" />
      </div>
    </div>
  </div>

</template>

<script>
import SearchBox from '@comp/basic/SearchBox.vue';
import BusinessCard from '@comp/basic/BusinessCard.vue';

export default {
  components: {
    SearchBox, BusinessCard,
  },
  data() {
    return {
      businessInfo: {
        name: '咖啡小馆',
        category: '咖啡厅',
        address: '市中心路123号',
        city: '成都',
        isOpen: true,
        image: 'path/to/image.jpg',
        reviewsCount: 120,
        rating: 4.5,
        businessHours: '08:00 - 18:00',
        features: ['免费Wi-Fi', '宠物友好', '户外座位'],
      },
    };
  },
  methods: {

  },
};
</script>

<style>
</style>
