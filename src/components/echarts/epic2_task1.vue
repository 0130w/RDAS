<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '700px', height: '400px' }"
  ></div>
</template>

<script>
// 分析每年加入的用户数量
export default {
  mounted() {
    this.draw();
  },
  methods: {
    draw() {
      // 初始化echarts实例
      const myChart = this.$echarts.init(document.getElementById('myChart'));

      // 原始柱状图数据
      const barData = [90, 937, 5423, 15340, 31097, 64911, 109054, 176435, 195955, 209762, 233465, 247850, 217620, 151024, 133568, 104655, 47444, 40485, 2782];

      // 计算增长率
      const growthRate = barData.map((item, index, array) => {
        if (index === 0) return 0; // 第一个元素没有前一个元素，所以增长率为0
        return ((item - array[index - 1]) / array[index - 1]) * 100; // 当前元素相对于前一个元素的增长率
      });

      // 绘制图表
      const option = {
        backgroundColor: 'transparent',
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
          data: [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
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
