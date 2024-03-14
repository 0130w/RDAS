<template>
  <div class="max-w-base rounded overflow-hidden shadow-lg">
    <div class="bg-gray-100 px-6 py-4 flex items-center">
      <a-select
        show-search
        v-model="searchTerm"
        placeholder="Search..."
        class="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg block w-full appearance-none leading-normal"
        @search="handleInput"
        @select="handleSelect"
        filter-option="false"
      >
        <a-select-option
          v-for="item in searchSuggestions"
          :key="item"
          :value="item"
        >
          {{ item }}
        </a-select-option>
      </a-select>
      <button
        @click="handleSearch"
        class="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
      >
        Search
      </button>
    </div>
    <div class="bg-gray-100 px-6 pb-4 flex justify-between items-center">
      <!-- 左侧条件选择 -->
      <Nav>
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
      style="max-height: 400px; overflow-y: auto;"
    >
      <List>
        <ListItem
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
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

export default {
  components: {
    Nav, NavItem, List, ListItem,
  },
  data() {
    return {
      searchTerm: '',
      searchSuggestions: ['推荐1', '推荐2', '推荐3'],
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
      movies: [
        {
          id: 1,
          title: 'The Shawshank Redemption',
          rating: 2.6,
          starRating: 2.6,
          year: 1994,
          genre: 'Drama',
          runtime: '2h 22min',
          cast: 'Tim Robbins, Morgan Freeman, Bob Gunton',
        },
        {
          id: 2,
          title: 'The Shawshank Redemption',
          rating: 2.6,
          starRating: 2.6,
          year: 1994,
          genre: 'Drama',
          runtime: '2h 22min',
          cast: 'Tim Robbins, Morgan Freeman, Bob Gunton',
        },
        {
          id: 3,
          title: 'The Shawshank Redemption',
          rating: 2.6,
          starRating: 2.6,
          year: 1994,
          genre: 'Drama',
          runtime: '2h 22min',
          cast: 'Tim Robbins, Morgan Freeman, Bob Gunton',
        },
        {
          id: 4,
          title: 'The Shawshank Redemption',
          rating: 2.6,
          starRating: 2.6,
          year: 1994,
          genre: 'Drama',
          runtime: '2h 22min',
          cast: 'Tim Robbins, Morgan Freeman, Bob Gunton',
        },
        {
          id: 5,
          title: 'The Shawshank Redemption',
          rating: 2.6,
          starRating: 2.6,
          year: 1994,
          genre: 'Drama',
          runtime: '2h 22min',
          cast: 'Tim Robbins, Morgan Freeman, Bob Gunton',
        },
      ],
    };
  },
  methods: {
    handleInput(event) {
      this.searchTerm = event.target.value;
    },
    handleSelect(value) {
      console.log(`Selected: ${value}`);
    },
    handleSearch() {
      console.log(`Searching for: ${this.searchTerm}`);
      // 执行搜索操作
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
