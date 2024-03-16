<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '700px', height: '400px' }"
  ></div>
</template>

<script>
// 统计出每年的tips数
export default {
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
          data: [2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
            2022],
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
            data: [665,
              26712,
              83395,
              110459,
              107563,
              109160,
              89686,
              94333,
              93909,
              67033,
              57646,
              32436,
              34993,
              925],
            type: 'bar',
            label: {
              show: true, // 显示标签
              position: 'top', // 标签的位置
              // 可以添加更多样式配置，如字体大小、颜色等
            },
          },
          // 添加的折线图配置
          {
            data: [665,
              26712,
              83395,
              110459,
              107563,
              109160,
              89686,
              94333,
              93909,
              67033,
              57646,
              32436,
              34993,
              925],
            type: 'line',
            smooth: true, // 可选，让折线平滑
            itemStyle: {
              color: 'red', // 折线颜色
            },
            lineStyle: {
              width: 2, // 线条宽度
            },
            symbol: 'circle', // 标记的形状
            symbolSize: 8, // 标记的大小
            showSymbol: true, // 是否显示标记
          },
        ],
      };
      // 设置option
      myChart.setOption(option);
    },

  },
};

</script>
