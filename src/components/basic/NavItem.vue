<template>
  <li>
    <a :class="['block px-3 py-2 rounded-md bg-gray-200', isActive ? 'bg-blue-500 text-white' : 'bg-slate-50']">
      <slot></slot>
    </a>
  </li>
</template>

<script>
export default {
  props: {
    isActive: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    toggleActive() {
      this.$emit('update:isActive', !this.isActive);
    },
  },
};
</script>
