<template>
  <div class="app-footer">
    
  </div>
</template>

<script>
export default {
  name: 'AppFooter',

  data: () => ({
    projectUrl: process.env.VUE_APP_PROJECT_URL,
    docUrl: process.env.VUE_APP_DOC_URL,
  }),
}
</script>

<style lang="scss" scoped>
.app-footer {
  @apply flex justify-between items-center text-gray-500;
  height: $footer-height;
}
</style>
