<template>
  <div class="chart-container p-4 mx-auto bg-white rounded-lg shadow-lg">
    <div
      ref="chart"
      class="chart"
      style="height: 400px; width: 600px;"
    ></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'YearlyCommentsChart',
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = this.$refs.chart;
      const myChart = echarts.init(chartDom);

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
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: ['评论数'],
        },
        xAxis: [
          {
            type: 'category',
            data: ['2019', '2020', '2021', '2022', '2023'],
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
            interval: 50,
            axisLabel: {
              formatter: '{value} 条',
            },
          },
        ],
        series: [
          {
            name: '评论数',
            type: 'bar',
            data: [150, 230, 224, 218, 135],
          },
          {
            name: '评论数',
            type: 'line',
            data: [150, 230, 224, 218, 135],
          },
        ],
      };

      myChart.setOption(option);
    },
  },
};
</script>

  <style scoped>
  /* 这里可以添加一些额外的CSS样式，
