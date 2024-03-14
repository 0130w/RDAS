<template>
  <div>
    <TopmenuVue
      :menu-items="menuItems"
      :content-components="contentComponents"
    />
  </div>
</template>

<script>
import exampleVue from '@comp/echarts/example.vue';
import TopmenuVue from '../../components/basic/Topmenu.vue';

export default {
  components: {
    TopmenuVue,
  },
  data() {
    return {
      menuItems: [
        {
          key: '1',
          title: '菜单1',
          children: [
            {
              label: 'Option 1',
              key: '2',
            },
            {
              label: 'Option 2',
              key: '3',
            },
          ],
        },
      ],
    };
  },
  computed: {
    contentComponents() {
      return {
        1: exampleVue, // 直接引用组件对象
        2: exampleVue,
        3: exampleVue,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
