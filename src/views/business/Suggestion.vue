<template>
  <div class="flex">
    <!-- 左侧内容 -->
    <div class="w-3/7 h-full p-4">
      <div class="bg-gray-200 h-full p-4 rounded-lg">
        <h1 class="text-2xl font-bold text-center mb-6">您的商户画像</h1>
        <BusinessCard
          v-if="businessInfo"
          :business="businessInfo"
        />
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="w-4/5 p-4">
      <div class="bg-gray-200 h-full p-4 rounded-lg">
        <SuggestionCardVue :data="SuggestionData" />
      </div>
    </div>
  </div>
</template>

<script>
import SuggestionCardVue from '@comp/basic/SuggestionCard.vue';
import BusinessCard from '@comp/basic/BusinessCard.vue';
import { getBusinessInfo, getSuggestion } from '@/api/business';

export default {
  components: {
    SuggestionCardVue, BusinessCard,
  },
  data() {
    return {
      businessInfo: null, // 初始值设为null
      SuggestionData: {
        services: [
          { name: '免费Wi-Fi', detail: '30%的更成功商家提供了此项服务' },
          { name: '停车位', detail: '' },
          { name: '信用卡支付', detail: '' },
        ],
        regionalImpacts:
        {
          title: '经营建议',
          description: '',
        },
      },
    };
  },
  computed: {
    info() {
      return this.$store.state.user.info;
    },
  },
  methods: {
    async getBusinessInfo() {
      const { business_id } = this.info;
      try {
        const response = await getBusinessInfo({ business_id });
        this.businessInfo = response.data.businessInfo;
        console.log('商户信息:', this.businessInfo);
      } catch (error) {
        console.error('获取商户信息失败:', error);
      }
    },
    async getSuggestion() {
      try {
        const response = await getSuggestion();
        this.SuggestionData.regionalImpacts.description = response.data.suggestionText;
      } catch (error) {
        console.error('获取商户经营建议失败:', error);
      }
    },
  },
  mounted() {
    this.getBusinessInfo();
    this.getSuggestion();
  },
};
</script>

<style scoped>
</style>
