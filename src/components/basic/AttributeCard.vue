<template>
  <div class="px-6 py-4">
    <div class="font-bold mb-2">商户信息</div>
    <ul class="list-disc pl-5">
      <li
        v-for="(attr, index) in formattedAttributes"
        :key="index"
      >
        {{ attr }}
      </li>
    </ul>
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
    formattedAttributes() {
      const attrs = this.business.attributes;
      const formatted = [];

      // 对于简单的布尔值属性
      formatted.push(`外送服务：${attrs.RestaurantsDelivery === 'True' ? '有' : '无'}`);
      formatted.push(`户外座位：${attrs.OutdoorSeating === 'True' ? '有' : '无'}`);
      formatted.push(`接受信用卡：${attrs.BusinessAcceptsCreditCards === 'True' ? '是' : '否'}`);
      formatted.push(`自行车停放：${attrs.BikeParking === 'True' ? '是' : '否'}`);
      formatted.push(`外卖服务：${attrs.RestaurantsTakeOut === 'True' ? '是' : '否'}`);
      formatted.push(`仅限预约：${attrs.ByAppointmentOnly === 'True' ? '是' : '否'}`);
      formatted.push(`提供餐饮：${attrs.Caters === 'True' ? '是' : '否'}`);

      // 对于更复杂的属性（如Parking）
      const parking = JSON.parse(attrs.BusinessParking.replace(/'/g, '"'));
      const parkingTypes = Object.keys(parking).filter((type) => parking[type] === true).join(', ');
      formatted.push(`停车服务：${parkingTypes.length > 0 ? parkingTypes : '无'}`);

      // 其他属性
      formatted.push(`Wi-Fi：${attrs.WiFi.replace(/u'/g, "'")}`);
      formatted.push(`酒精饮料：${attrs.Alcohol.replace(/u'/g, "'")}`);
      formatted.push(`价格范围：${attrs.RestaurantsPriceRange2}`);

      return formatted;
    },
  },

};
</script>

<style>
</style>
