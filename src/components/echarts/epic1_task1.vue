<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '700px', height: '400px' }"
  ></div>
</template>

<script>
// 找出美国最常见商户（前20）
export default {
  // 钩子函数
  mounted() {
    this.draw();
  },
  methods: {
    draw() {
      // 初始化echarts实例
      const myChart = this.$echarts.init(document.getElementById('myChart'));
      // 绘制图表
      const option = {
        xAxis: {
          type: 'category',
          data: ['Starbucks', "McDonald's", "Dunkin'", 'Subway', 'Taco Bell', 'CVS Pharmacy', 'Walgreens', 'Burger King', "Wendy's", 'Wawa', "Domino's Pizza", 'The UPS Store', 'Pizza Hut', 'Enterprise Rent-A-Car', "Papa John's Pizza", 'Great Clips', "Jimmy John's", 'US Post Office', 'KFC', 'Chick-fil-A'],
          axisLabel: {
            rotate: 90, // 旋转角度
          },
          name: '种类',
        },
        yAxis: {
          type: 'value',
          name: '数量',
        },
        series: [
          {
            data: [724, 703, 510, 459, 365, 345, 341, 338, 331, 307, 295, 281, 272, 232, 196, 185, 175, 174, 171, 162],
            type: 'bar',
            label: {
              show: true, // 显示标签
              position: 'top', // 标签的位置
              // 可以添加更多样式配置，如字体大小、颜色等
            },
          },
        ],
      };
      // 设置option
      myChart.setOption(option);
    },
  },
};
</script>
