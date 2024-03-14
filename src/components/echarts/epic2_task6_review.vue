<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '700px', height: '400px' }"
  ></div>
</template>

<script>
// 统计出每年的评论数
export default {
  mounted() {
    this.draw();
  },
  methods: {
    draw() {
      // 初始化echarts实例
      const myChart = this.$echarts.init(document.getElementById('myChart'));

      // 原始柱状图数据
      const barData = [120, 200, 150, 80, 70];

      // 计算增长率
      const growthRate = barData.map((item, index, array) => {
        if (index === 0) return 0; // 第一个元素没有前一个元素，所以增长率为0
        return ((item - array[index - 1]) / array[index - 1]) * 100; // 当前元素相对于前一个元素的增长率
      });

      // 绘制图表
      const option = {
        tooltip: {
          trigger: 'axis',
          // 显示增长率的百分比格式
          formatter(params) {
            let result = `${params[0].name}<br/>`;
            params.forEach((item) => {
              if (item.seriesType === 'line') {
                // 对于折线图（增长率），显示百分比
                result += `${item.marker} ${item.seriesName}: ${item.value.toFixed(2)}%<br/>`;
              } else {
                // 对于其他类型（柱状图），显示原始值
                result += `${item.marker} ${item.seriesName}: ${item.value}<br/>`;
              }
            });
            return result;
          },
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
          axisLabel: {
            rotate: 90, // 旋转角度
          },
          name: '种类',
        },
        yAxis: {
          type: 'value',
          name: '数量/增长率 (%)',
        },
        series: [
          {
            name: '数量',
            data: barData,
            type: 'bar',
            label: {
              show: true, // 显示标签
              position: 'top', // 标签的位置
              // 可以添加更多样式配置，如字体大小、颜色等
            },
          },
          {
            name: '增长率',
            data: growthRate,
            type: 'line', // 添加折线图系列
            smooth: true, // 可以设置为true使折线平滑
          },
        ],
      };

      // 设置option
      myChart.setOption(option);
    },
  },
};

</script>
