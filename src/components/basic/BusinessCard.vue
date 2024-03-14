<template>
  <div class="rounded overflow-hidden shadow-lg bg-white">
    <img
      class="w-full h-64 object-cover"
      :src="business.image"
      alt="商户图片"
    >
    <div class="px-6 py-4 flex flex-wrap justify-between items-start">
      <div>
        <div class="font-bold text-xl mb-2">{{ business.name }}</div>
        <p class="text-gray-700 text-base">{{ business.category }} | {{ business.city }}</p>
        <p class="text-gray-600 text-sm">{{ business.address }}</p>
        <div class="mt-2">
          <span
            v-if="business.isOpen"
            class="inline-block bg-green-200 rounded-full px-3 py-1 text-sm font-semibold text-green-700 mr-2"
          >正在营业</span>
          <span
            v-else
            class="inline-block bg-red-200 rounded-full px-3 py-1 text-sm font-semibold text-red-700 mr-2"
          >已打烊</span>
          <span class="inline-block bg-blue-200 rounded-full px-3 py-1 text-sm font-semibold text-blue-700">营业时间：{{ business.businessHours }}</span>
        </div>
      </div>
      <div class="flex flex-col items-end">
        <span class="block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-yellow-700 mb-2">{{ business.reviewsCount }} 评论</span>
        <span class="flex bg-indigo-200 rounded-full px-3 py-1 text-sm font-semibold text-indigo-700 items-center">
          <svg
            width="16"
            height="20"
            fill="currentColor"
          >
            <path d="M7.05 3.691c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.372 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.539 1.118l-2.8-2.034a1 1 0 00-1.176 0l-2.8 2.034c-.783.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.363-1.118L.98 9.483c-.784-.57-.381-1.81.587-1.81H5.03a1 1 0 00.95-.69L7.05 3.69z" />
          </svg>
          {{ business.rating }}
        </span>
      </div>

    </div>
    <div class="px-6 pb-2">
      <h3 class="text-lg mb-2">特色:</h3>
      <ul>
        <li
          v-for="(feature, index) in business.features"
          :key="index"
          class="text-gray-600 text-sm list-disc ml-4"
        >{{ feature }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    business: {
      type: Object,
      required: true,
    },
  },
};
</script>
