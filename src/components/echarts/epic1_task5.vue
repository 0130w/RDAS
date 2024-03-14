<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '800px', height: '400px' }"
  ></div>
</template>

<script>

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
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999',
            },
          },
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true,
        },
        xAxis: [
          {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            axisPointer: {
              type: 'shadow',
            },
          },
        ],
        yAxis: [
          {
            type: 'value',
            name: '数量',
            min: 0,
            max: 250,
            position: 'left',
            axisLabel: {
              formatter: '{value}',
            },
          },
          {
            type: 'value',
            name: '评分',
            min: 0,
            max: 5, // 根据次要维度数据的范围设定
            position: 'right',
            inverse: true, // 反向坐标轴
            axisLabel: {
              formatter: '{value}',
            },
          },
        ],
        series: [
          {
            name: '数量',
            type: 'bar',
            data: [120, 200, 150, 80, 70, 120, 200, 150, 80, 70],
          },
          {
            name: '评分',
            type: 'bar',
            yAxisIndex: 1, // 使用次要维度的y轴
            data: [2.3, 1.8, 3.2, 2.6, 2.4, 2.7, 1.7, 3.1, 2.9, 1.6],
          },
        ],
      };

      // 设置option
      myChart.setOption(option);
    },
  },
};
</script>
