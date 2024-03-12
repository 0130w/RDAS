<template>
  <div class="search-box">
    <input
      type="text"
      placeholder="Search..."
      v-model="searchTerm"
      @input="handleInput"
    />
    <button @click="handleSearch">Search</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchTerm: '',
    };
  },
  methods: {
    handleInput(event) {
      this.searchTerm = event.target.value;
    },
    handleSearch() {
      // 执行搜索操作
      console.log('Searching for:', this.searchTerm);
    },
  },
};
</script>

<style scoped>
.search-box {
  display: flex;
  align-items: center;
}

input[type="text"] {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  margin-left: 8px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0056b3;
}
</style>
