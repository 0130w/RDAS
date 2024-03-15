<template>
  <div class="flex">
    <!-- 左侧内容 -->
    <div class="w-4/7 h-full p-2">
      <!-- 这里放置左侧的内容 -->
      <div class="bg-gray-100 h-full p-4 rounded-lg">
        <SearchBox @select-business="handleSelectBusiness" />
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="w-3/7 p-4">
      <!-- 这里放置右侧的内容 -->
      <div class="bg-gray-100 h-full p-2 rounded-lg">
        <BusinessCard
          v-if="businessInfo"
          :business="businessInfo"
        />
      </div>
    </div>
  </div>

</template>

<script>
import SearchBox from '@comp/basic/SearchBox.vue';
import BusinessCard from '@comp/basic/BusinessCard.vue';
import Axios from 'axios';

export default {
  components: {
    SearchBox, BusinessCard,
  },
  data() {
    return {
      businessInfo: null, // 初始化为null
    };
  },
  methods: {
    async handleSelectBusiness(business_id) {
      console.log('Selected business ID:', business_id);
      try {
        // 向后端发送请求获取businessInfo
        const response = await Axios.get('/business/getBusinessInfo', business_id);
        this.businessInfo = response.data.data.businessInfo; // 更新businessInfo数据
      } catch (error) {
        console.error('Error fetching business info:', error);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
