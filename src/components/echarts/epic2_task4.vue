<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '1100px', height: '450px' }"
  ></div>
</template>

<script>
// 统计每年优质用户、普通用户比例
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
          data: ['优质用户', '普通用户'],
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
            data: [120, 200],
            type: 'bar',
          },
        ],
      };
      // 设置option
      myChart.setOption(option);
    },
  },
};
</script>
