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
          <a-sub-menu
            v-for="menu in menuItems"
            :key="menu.key"
            :title="menu.title"
          >
            <a-menu-item
              v-for="item in menu.children"
              :key="item.key"
            >
              {{ item.title }}
            </a-menu-item>
          </a-sub-menu>
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
export default {
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
      // 初始化为第一个菜单项的第一个子项（如果存在）
      currentKey: this.menuItems.length > 0 && this.menuItems[0].children.length > 0
        ? this.menuItems[0].children[0].key
        : null,
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
