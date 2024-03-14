<template>
  <div class="mx-auto mt-5">
    <a-card class="rounded-lg shadow">
      <template #title>
        <a-menu
          mode="horizontal"
          @click="handleMenuClick"
          :selected-keys="[currentKey]"
          class="border-b"
        >
          <a-menu-item
            v-for="item in menuItems"
            :key="item.key"
          >
            {{ item.title }}
          </a-menu-item>
        </a-menu>
      </template>
      <component
        :is="currentComponent"
        class="mt-4 rounded-lg shadow"
      ></component>
    </a-card>
  </div>
</template>

<script>
import exampleVue from '@comp/echarts/example.vue';

export default {
  components: {
    exampleVue,
  },
  props: {
    menuItems: {
      type: Array,
      required: true,
    },
    contentComponents: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      currentKey: this.menuItems[0].key, // 默认显示第一个菜单项的内容
    };
  },
  computed: {
    currentComponent() {
      // 根据currentKey返回相应的组件
      return this.contentComponents[this.currentKey];
    },
  },
  methods: {
    handleMenuClick(e) {
      this.currentKey = e.key;
    },
  },
};
</script>
