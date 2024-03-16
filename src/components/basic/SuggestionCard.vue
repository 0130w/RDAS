<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold text-center mb-6">如何让您的店铺更成功</h1>
    <div class="bg-white shadow-md rounded-lg p-6">
      <p class="text-lg mb-4">成功的商家通常提供以下服务：</p>
      <ul class="list-disc list-inside mb-6">
        <li
          v-for="(item, index) in data.services"
          :key="index"
        >{{ item.name }} - {{ item.detail }}</li>
      </ul>
      <!-- 由于regionalImpacts现在是对象，我们直接访问其属性而不是遍历 -->
      <div>
        <h2 class="text-xl font-semibold mb-4">{{ data.regionalImpacts.title }}</h2>
        <p>{{ data.regionalImpacts.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      required: true,
      default: () => ({}),
    },
  },
};
</script>

<style scoped>
</style>
