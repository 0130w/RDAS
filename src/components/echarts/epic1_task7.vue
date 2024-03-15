<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '700px', height: '400px' }"
  ></div>
</template>

<script>
// 统计最多的category及数量（前10）
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
          data: ['Beauty & Spas, Nail Salons', 'Restaurants, Pizza', 'Nail Salons, Beauty & Spas', 'Pizza, Restaurants', 'Restaurants, Mexican', 'Restaurants, Chinese', 'Mexican, Restaurants', 'Chinese, Restaurants', 'Food, Coffee & Tea', 'Beauty & Spas, Hair Salons'],
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
            data: [1012, 935, 934, 823, 728, 708, 672, 651, 508, 493],
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
