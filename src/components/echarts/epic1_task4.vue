<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '1100px', height: '450px' }"
  ></div>
</template>

<script>
// 找出美国最常见商户，并显示平均评分（前20）
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
            data: ['Starbucks', "McDonald's", "Dunkin'", 'Subway', 'Taco Bell', 'CVS Pharmacy', 'Walgreens', 'Burger King', "Wendy's", 'Wawa', "Domino's Pizza", 'The UPS Store', 'Pizza Hut', 'Enterprise Rent-A-Car', "Papa John's Pizza", 'Great Clips', "Jimmy John's", 'US Post Office', 'KFC', 'Chick-fil-A'],
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
            data: [724, 703, 510, 459, 365, 345, 341, 338, 331, 307, 295, 281, 272, 232, 196, 185, 175, 174, 171, 162],
            label: {
              show: true, // 显示标签
              position: 'top', // 标签的位置
              // 可以添加更多样式配置，如字体大小、颜色等
            },
          },
          {
            name: '评分',
            type: 'bar',
            yAxisIndex: 1, // 使用次要维度的y轴
            data: [3.126381215469613, 1.8634423897581793, 2.302941176470588, 2.5860566448801743, 2.154794520547945, 2.4565217391304346, 2.624633431085044, 2.0281065088757395, 2.015105740181269, 3.3192182410423454, 2.2813559322033896, 3.215302491103203, 2.0330882352941178, 3.2780172413793105, 2.4081632653061225, 2.9, 2.8685714285714288, 2.4195402298850577, 1.8596491228070176, 3.3858024691358026],
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
