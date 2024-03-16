<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '1100px', height: '450px' }"
  ></div>
</template>

<script>
// 统计评分最高的城市（前10）
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
          data: ['AB Edmonton', 'MARLTON', 'Chestnut Hill', 'Bucks', 'Merion Park', 'St.Pete Beach', 'Worcester', 'Harleysville', 'Westampton', 'TAMPA AP'],
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
            data: [4.5, 4.5, 4.5, 4.0625, 3.5, 3.5, 3.5625, 3.38265306122449, 2.9166666666666665, 2.0],
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
