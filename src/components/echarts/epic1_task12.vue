<template>
  <!-- 一定要设置宽高,且宽高必须是行内样式，单位必须是px -->
  <div
    id="myChart"
    :style="{ width: '600px', height: '300px' }"
  ></div>
</template>

<script>
// 找出美国商户最多的前10个城市

import * as echarts from 'echarts';

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
        color: ['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'],

        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985',
            },
          },
        },
        legend: {
          data: ['American', 'MeciMexican', 'Chinese'],
        },
        toolbox: {
          feature: {
            saveAsImage: {},
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
            boundaryGap: false,
            data: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
            name: '种类',
          },

        ],
        yAxis: [
          {
            type: 'value',
            name: '留存量',
          },
        ],
        series: [
          {
            name: 'Line 1',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0,
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(128, 255, 165)',
                },
                {
                  offset: 1,
                  color: 'rgb(1, 191, 236)',
                },
              ]),
            },
            emphasis: {
              focus: 'series',
            },
            data: [1, 4348, 1642, 1046, 887, 765, 801, 641, 597, 516, 494, 321, 301, 6],
          },
          {
            name: 'Line 2',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0,
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(0, 221, 255)',
                },
                {
                  offset: 1,
                  color: 'rgb(77, 119, 255)',
                },
              ]),
            },
            emphasis: {
              focus: 'series',
            },
            data: [0, 1221, 581, 318, 285, 311, 278, 290, 295, 260, 289, 203, 216, 7],
          },
          {
            name: 'Line 3',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0,
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(55, 162, 255)',
                },
                {
                  offset: 1,
                  color: 'rgb(116, 21, 219)',
                },
              ]),
            },
            emphasis: {
              focus: 'series',
            },
            data: [0, 865, 626, 368, 247, 186, 156, 129, 115, 103, 99, 46, 54, 1],
          },

        ],
      };
      // 设置option
      myChart.setOption(option);
    },
  },
};
</script>
