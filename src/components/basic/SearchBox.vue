<template>
  <div class="max-w-base rounded overflow-hidden shadow-lg max-w-2xl">
    <div class="bg-gray-100 px-6 py-4 flex items-center justify-between">
      <!-- 纬度输入框 -->
      <input
        type="text"
        class="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-1/4 appearance-none leading-normal"
        placeholder="Latitude"
        v-model="latitude"
        @input="handleLatitudeInput"
      />
      <!-- 经度输入框 -->
      <input
        type="text"
        class="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-1/4 appearance-none leading-normal"
        placeholder="Longitude"
        v-model="longitude"
        @input="handleLongitudeInput"
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
      style="height: 400px; overflow-y: auto;"
    >
      <List v-if="businesses">
        <ListItem
          v-for="business in businesses"
          :key="business.id"
          :business="business"
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
import Axios from 'axios';

export default {
  components: {
    Nav, NavItem, List, ListItem,
  },
  data() {
    return {
      latitude: '',
      longitude: '',
      selectedCity: null,
      cities: [
        { value: 'beijing', label: 'Beijing' },
        { value: 'shanghai', label: 'Shanghai' },
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
        { value: 'option1', label: '选项1' },
        { value: 'option2', label: '选项2' },
        { value: 'option3', label: '选项3' },
        { value: 'option4', label: '选项4' },
      ],
      businesses: [

      ],
    };
  },
  mounted() {
    Axios.get('/user/recommendByHistory')
      .then((response) => {
        this.businesses = response.data.data.businesses;
      });
  },
  methods: {
    handleLatitudeInput() {
      // 处理纬度输入
    },
    handleLongitudeInput() {
      // 处理经度输入
    },
    handleCityChange(value) {
      // 处理城市选择
      console.log('Selected city:', value);
    },
    handleSelect(value) {
      console.log(`Selected: ${value}`);
    },
    async handleSearch(latitude, longitude, selectedCity) {
      console.log('Searching for:', { latitude, longitude, selectedCity });
      if (latitude && longitude && selectedCity) { // 确保所有值都已提供
        this.loading = true;
        try {
          // 构建搜索参数
          const searchParams = {
            latitude,
            longitude,
            city: selectedCity,
          };
          // 发起搜索请求，这里假设你有一个对应的action来处理搜索
          const response = await this.$store.dispatch('user/searchForBusiness', searchParams);
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
    toggleItem(value) {
      if (this.selectedItems.includes(value)) {
        this.selectedItems = this.selectedItems.filter((item) => item !== value);
      } else {
        this.selectedItems.push(value);
      }
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
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
