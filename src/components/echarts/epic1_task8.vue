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
          data: ['Belmond El Encanto', 'Huong Sizzling Wok', "Slizzy Mcgee's", 'Mi Tenampa', 'Wayback Burgers', "Elicia's Pizza", 'Bangkok Express', 'Red Zone 2', 'Dry-At-Last-Waterproofing', 'Freebirds', 'Suppa', 'Rose Endodontics', 'Tire Techs USA', 'Hopewell Road Pharmacy', 'Curb Appeal Auto Detailing', "Bagger Dave's Burger Tavern", 'Alenco Fence & Lumber', 'Gin & Pop', 'Finders Keepers', 'Hollywood Cafe & Sports Bar'],
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
            data: [203, 50, 47, 38, 37, 23, 8, 8, 6, 5, 5, 4, 4, 4, 3, 3, 2, 2, 2, 2],
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
