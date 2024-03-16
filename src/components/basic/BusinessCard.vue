<template>
  <div
    class="rounded overflow-hidden shadow-lg bg-white p-2"
    style="width: 450px;"
  >
    <img
      class="w-full h-64 object-cover p-4"
      src="../../assets/images/OIP-C.jpg"
      alt="商户图片"
    >
    <div class="px-6 py-2 font-bold text-xl">{{ business.name }}</div>
    <div class="px-6 py-2 flex flex-wrap justify-between items-start">
      <div>
        <p class="text-gray-700 text-base">City: {{ business.city }}</p>
        <p class="text-gray-600 text-sm">Address: {{ business.address }}</p>
        <div class="mt-2">
          <span
            v-if="business.is_open === 1"
            class="inline-block bg-green-200 rounded-full px-3 py-1 text-sm font-semibold text-green-700 mr-2"
          >正在营业</span>
          <span
            v-else
            class="inline-block bg-red-200 rounded-full px-3 py-1 text-sm font-semibold text-red-700 mr-2"
          >已打烊</span>
          <span class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-yellow-700 mb-2">{{ business.review_count }} reviews</span>

        </div>
      </div>
      <div class="flex flex-col items-end">
        <span class="flex bg-indigo-200 rounded-full px-3 py-1 text-xl font-semibold text-indigo-700 items-center">
          <svg
            width="16"
            height="20"
            fill="currentColor"
          >
            <path d="M7.05 3.691c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.372 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.539 1.118l-2.8-2.034a1 1 0 00-1.176 0l-2.8 2.034c-.783.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.363-1.118L.98 9.483c-.784-.57-.381-1.81.587-1.81H5.03a1 1 0 00.95-.69L7.05 3.69z" />
          </svg>
          {{ business.stars }}
        </span>
      </div>
    </div>
    <div class="px-6 py-2">
      <div class="font-bold mb-2">Categories: </div>
      <div>{{ business.categories }}</div>
    </div>
    <div
      class="px-6 py-2"
      v-if="Object.keys(formattedBusinessHours).length > 0"
    >
      <div class="font-bold mb-2">营业时间</div>
      <ul class="list-disc pl-5">
        <li
          v-for="(time, day) in formattedBusinessHours"
          :key="day"
        >
          {{ day }}: {{ time }}
        </li>
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
  computed: {
    formattedBusinessHours() {
      const { hours } = this.business;
      if (!hours) { // 如果hours为null或undefined，则返回空对象
        return {};
      }
      const formatted = {};
      Object.keys(hours).forEach((day) => {
        const time = hours[day];
        if (time === '0:0-0:0') {
          formatted[day] = '休息';
        } else {
          const [start, end] = time.split('-');
          const formattedStart = this.formatTime(start);
          const formattedEnd = this.formatTime(end);
          formatted[day] = `${formattedStart} - ${formattedEnd}`;
        }
      });
      return formatted;
    },
  },
  methods: {
    formatTime(time) {
      const [hours, minutes] = time.split(':');
      return `${hours.padStart(2, '0')}:${minutes.padStart(2, '0')}`;
    },
  },
};
</script>
