<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '700px', height: '400px' }"
  ></div>
</template>

<script>
// 收获五星评论最多的商户（前20）
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
          data: ['Hollywood Cafe & Sports Bar', 'Alenco Fence & Lumber', 'Finders Keepers', 'Mi Tenampa', 'Curb Appeal Auto Detailing', "Bagger Dave's Burger Tavern", 'Tire Techs USA', 'Hopewell Road Pharmacy', 'Rose Endodontics', 'Dry-At-Last-Waterproofing', 'Gin & Pop', 'Red Zone 2', 'Suppa', 'Freebirds', "Elicia's Pizza", 'Belmond El Encanto', 'Bangkok Express', 'Huong Sizzling Wok', 'Wayback Burgers', "Slizzy Mcgee's"],
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
            data: [23, 5, 2, 38, 8, 4, 8, 4, 6, 5, 37, 3, 50, 2, 5, 203, 4, 47, 2, 3],
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
