<template>
  <div class="flex flex-col items-center p-4 bg-white shadow-lg rounded-lg">
    <!-- 下拉选择菜单 -->
    <a-select
      v-model="selectedYear"
      style="width: 120px"
      class="mb-5"
      @change="updateChart"
    >
      <a-select-option value="2020">2020</a-select-option>
      <a-select-option value="2019">2019</a-select-option>
      <a-select-option value="2018">2018</a-select-option>
    </a-select>

    <!-- 图表 -->
    <div
      ref="ratingsChart"
      class="w-full"
      style="height: 347px; width: 500px;"
    ></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import ASelect from 'ant-design-vue/lib/select';

export default {
  name: 'CommentRatingsChart',
  components: {
    ASelect,
    ASelectOption: ASelect.Option,
  },
  data() {
    return {
      selectedYear: '2020',
      myChart: null,
    };
  },
  mounted() {
    this.myChart = echarts.init(this.$refs.ratingsChart);
    this.updateChart();
  },
  methods: {
    initChart(option) {
      this.myChart.setOption(option);
    },
    updateChart() {
      const option = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)',
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: ['有用', '有趣', '酷'],
        },
        series: [
          {
            name: '评论标记',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center',
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '18',
                fontWeight: 'bold',
              },
            },
            labelLine: {
              show: false,
            },
          },
        ],
      };

      // 基于selectedYear更新图表数据
      option.series[0].data = this.getDataByYear(this.selectedYear);

      this.initChart(option);
    },
    getDataByYear(year) {
      const data = {
        2020: [
          { value: 1048, name: '有用' },
          { value: 735, name: '有趣' },
          { value: 580, name: '酷' },
        ],
        2019: [
          // 不同的数据
          { value: 200, name: '有用' },
          { value: 735, name: '有趣' },
          { value: 580, name: '酷' },
        ],
        2018: [
          // 不同的数据
          { value: 100, name: '有用' },
          { value: 735, name: '有趣' },
          { value: 580, name: '酷' },
        ],
      };
      return data[year];
    },
  },
};
</script>

<style scoped>
/* Tailwind CSS在此处已经通过CDN或构建工具引入，你可以直接使用它的类 */
</style>
