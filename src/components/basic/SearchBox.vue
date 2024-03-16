<template>
  <div class="max-w-base rounded overflow-hidden shadow-lg max-w-2xl">
    <div class="bg-gray-100 px-6 py-4 flex items-center justify-between">
      <!-- 纬度输入框 -->
      <input
        type="text"
        class="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-1/4 appearance-none leading-normal"
        placeholder="Latitude"
        v-model="latitude"
      />
      <!-- 经度输入框 -->
      <input
        type="text"
        class="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-1/4 appearance-none leading-normal"
        placeholder="Longitude"
        v-model="longitude"
      />
      <!-- 城市下拉选项 -->
      <a-select
        v-model="selectedCity"
        class="w-1/4 max-w-xs"
        placeholder="Select a city"
        @change="handleCityChange"
      >
        <a-select-option
          v-for="city in cities"
          :key="city.value"
          :value="city.value"
        >
          {{ city.label }}
        </a-select-option>
      </a-select>
      <button
        @click="handleSearch(latitude, longitude, selectedCity)"
        class=" ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
      >
        Search
      </button>
    </div>
    <div class="bg-gray-100 px-6 pb-4 flex justify-between items-center ">
      <!-- 左侧条件选择 -->
      <Nav class="mr-64">
        <NavItem
          v-for="choice in choices"
          :key="choice.value"
          :is-active="choice.isActive"
          @click.native="() => changeChoice(choice)"
        >
          {{ choice.label }}
        </NavItem>
      </Nav>
      <!-- 右侧筛选按钮 -->
      <a-dropdown placement="bottomRight">
        <button
          type="button"
          class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-blue-500 hover:bg-blue-600 focus:outline-none focus:shadow-outline-blue focus:border-blue-700 active:bg-blue-700 transition ease-in-out duration-150"
        >
          <svg
            class="-ml-1 mr-1 h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M2 5a1 1 0 011-1h14a1 1 0 011 1v3a1 1 0 01-1 1H3a1 1 0 01-1-1V5zm0 7a1 1 0 011-1h7a1 1 0 011 1v3a1 1 0 01-1 1H3a1 1 0 01-1-1v-3zm10-2a1 1 0 100-2 1 1 0 000 2z"
              clip-rule="evenodd"
            />
          </svg>
          筛选
        </button>
        <a-menu slot="overlay">
          <a-menu-item-group>
            <template #title>
              <a-checkbox
                v-model="selectAll"
                @change="toggleSelectAll"
              >全选</a-checkbox>
            </template>
            <a-menu-item
              v-for="option in options"
              :key="option.value"
            >
              <a-checkbox
                :checked="isChecked(option.value)"
                @change="toggleItem(option.value)"
              >
                {{ option.label }}
              </a-checkbox>
            </a-menu-item>
          </a-menu-item-group>
        </a-menu>
      </a-dropdown>
    </div>
    <div
      class="h-80 overflow-auto"
      style="height: 600px; overflow-y: auto;"
    >
      <List v-if="businesses">
        <ListItem
          v-for="business in filteredBusinesses"
          :key="business.id"
          :business="business"
          @select-business="handleSelectBusiness"
        />
      </List>
    </div>
  </div>
</template>

<script>
import Nav from '@comp/basic/Nav.vue';
import NavItem from '@comp/basic/NavItem.vue';
import List from '@comp/basic/List.vue';
import ListItem from '@comp/basic/ListItem.vue';
import { getToken } from '@/utils/token';

export default {
  components: {
    Nav, NavItem, List, ListItem,
  },
  data() {
    return {
      latitude: '34.4266787',
      longitude: '-119.7111968',
      selectedCity: 'Santa Barbara',
      cities: [
        { value: 'Santa Barbara', label: 'Santa Barbara' },
        { value: 'Philadelphia', label: 'Philadelphia' },
        { value: 'Green Lane', label: 'Green Lane' },
        { value: 'Ashland City', label: 'Ashland City' },
        { value: 'Brentwood Point', label: 'Brentwood Point' },
        { value: 'St. Petersburg', label: 'St. Petersburg' },
        { value: 'Affton', label: 'Affton' },
        { value: 'Nashville', label: 'Nashville' },
        { value: 'Land O\'Lakes', label: 'Land O\'Lakes' },
        { value: 'Largo', label: 'Largo' },
        // 更多城市...
      ],
      selectedItems: [],
      activeChoice: '0',
      choices: [
        { value: '0', label: '综合排序', isActive: true },
        { value: '1', label: '距离优先', isActive: false },
        { value: '2', label: '评分优先', isActive: false },
      ],
      selectAll: false,
      options: [
        { value: 'option1', label: '距离 < 0.5km' },
        { value: 'option2', label: '评分 > 3' },
        { value: 'option3', label: '正在营业' },
      ],
      businesses: [

      ],
    };
  },
  mounted() {
    this.recommendByHistory();
  },
  computed: {
    // 使用计算属性来根据筛选条件过滤businesses列表
    filteredBusinesses() {
      return this.businesses.filter((business) => {
        // 根据selectedItems中的值进行筛选
        let conditionsMet = true; // 假设所有条件都满足

        if (this.selectedItems.includes('option1')) {
          // 将distance字符串转换为数值
          const distance = parseFloat(business.distance);
          // 检查距离是否小于0.5km
          conditionsMet = conditionsMet && distance < 0.5;
        }
        if (this.selectedItems.includes('option2')) {
          // 如果选中“评分 > 3”
          conditionsMet = conditionsMet && business.stars > 3;
        }
        if (this.selectedItems.includes('option3')) {
          // 如果选中“正在营业”
          conditionsMet = conditionsMet && business.is_open;
        }

        return conditionsMet; // 只返回满足所有选中条件的business对象
      });
    },
  },
  methods: {
    handleCityChange(value) {
      // 处理城市选择
      console.log('Selected city:', value);
    },
    handleSelect(value) {
      console.log(`Selected: ${value}`);
    },
    async recommendByHistory() {
      try {
        const response = await this.$store.dispatch('recommendByHistory', getToken());
        this.businesses = response.businesses;
      } catch (error) {
        console.error(error);
      }
    },
    async handleSearch(latitude, longitude, selectedCity) {
      console.log('Searching for:', { latitude, longitude, selectedCity });
      // 获取当前选中的choice
      const selectedChoice = this.choices.find((choice) => choice.isActive).value;
      if (latitude && longitude && selectedCity) {
        this.loading = true;
        try {
          // 构建搜索参数，包括latitude, longitude, city, choice
          const searchParams = {
            latitude,
            longitude,
            city: selectedCity,
            choice: selectedChoice,
          };
          // 发起搜索请求，这里假设你有一个对应的action来处理搜索
          const response = await this.$store.dispatch('searchForBusiness', searchParams);
          if (response && response.businesses) {
            console.log(response);
            this.businesses = response.businesses;
          } else {
            this.$message.error('搜索未找到结果');
          }
        } catch (error) {
          console.error(error);
          this.$message.error('搜索过程中出现错误');
        } finally {
          this.loading = false;
        }
      } else {
        // 如果必要的搜索条件没有全部提供
        this.$message.error('请完整填写搜索条件');
      }
    },
    toggleItem(value) {
      const index = this.selectedItems.indexOf(value);
      if (index !== -1) {
        this.selectedItems.splice(index, 1); // 如果找到，则移除
      } else {
        this.selectedItems.push(value); // 否则添加到selectedItems中
      }
    },
    toggleSelectAll() {
      if (this.selectAll) {
        this.selectedItems = this.options.map((option) => option.value);
      } else {
        this.selectedItems = [];
      }
    },
    isChecked(value) {
      return this.selectedItems.includes(value);
    },
    changeChoice(clickedChoice) {
      this.activeChoice = clickedChoice.value;
      console.log(this.activeChoice);
      this.choices.forEach((choice) => {
        if (choice.value === clickedChoice.value) {
          // 当前点击的选项，设置isActive为true
          choice.isActive = true;
          console.log(choice.label, choice.isActive);
        } else {
          // 其他选项，设置isActive为false
          choice.isActive = false;
          console.log(choice.label, choice.isActive);
        }
      });
      // 在切换选项后自动执行搜索
      this.handleSearch(this.latitude, this.longitude, this.selectedCity);
    },
    handleSelectBusiness(businessId) {
      this.$emit('select-business', businessId);
      // 在这里处理选中的businessId，可以将其存储在父组件的data中或者进行其他操作
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
