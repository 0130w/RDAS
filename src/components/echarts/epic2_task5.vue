<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '1100px', height: '450px' }"
  ></div>
</template>

<script>
// 显示每年总用户数、沉默用户数（未写评论）的比例
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
          data: [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
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
            data: [0.8773125608568647, 0.8671317829457365, 0.8557595227168426, 0.8344961899899787, 0.8354301431263689, 0.83253398691658, 0.8260444794897926, 0.8377934123442616, 0.8268858992044539, 0.7989570912900048, 0.775978653340763, 0.7752608029900414, 0.7726320599073035, 0.7645435420642656, 0.7725916172689447, 0.8540694116618586, 0.8417033773861967, 0.9885954855809934],
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
