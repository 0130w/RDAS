<template>
  <div class="flex">
    <!-- 左侧内容 -->
    <div class="w-2/5 h-full p-4">
      <!-- 这里放置左侧的内容 -->
      <div class="bg-gray-100 h-full p-4 rounded-lg">
        <h1 class="text-2xl font-bold text-center mb-6">您的商户画像</h1>
        <BusinessCard :business="businessInfo" />
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="w-3/5 p-5">
      <!-- 这里放置右侧的内容 -->
      <div class="bg-gray-200 h-full p-4 rounded-lg">
        <SuggestionCardVue :data="SuggestionData" />
      </div>
    </div>
  </div>
</template>

<script>
import SuggestionCardVue from '@comp/basic/SuggestionCard.vue';
import BusinessCard from '@comp/basic/BusinessCard.vue';

export default {
  components: {
    SuggestionCardVue, BusinessCard,
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
      SuggestionData: {
        services: [
          { name: '叫醒服务', detail: '30%的更成功商家提供了此项服务' },
          { name: '免费Wi-Fi', detail: '' },
          { name: '停车位', detail: '' },
          { name: '信用卡支付', detail: '' },
          // 更多服务
        ],
        regionalImpacts: [
          {
            title: '地域影响',
            description: '不同地区的顾客可能对服务有不同的需求，考虑到地域特性进行服务调整，可以吸引更多顾客。',
          },
          // 更多地域影响
        ],
      },
    };
  },
};
</script>

  <style scoped>
</style>
