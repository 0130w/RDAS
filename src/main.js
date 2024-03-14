import Vue from 'vue';
import errorHandler from '@/utils/error-handler';
import * as echarts from 'echarts';
import VueResource from 'vue-resource';
import App from './App.vue';
import router from './router/router';
import store from './store/store';

import './router/control';
import './plugins';
import '@/assets/scss/reset.scss';
import '@/assets/scss/common.scss';
import './directives'; // 自定义指令
// 引入
// 将echarts添加到vue的原型上
Vue.prototype.$echarts = echarts;
Vue.config.errorHandler = errorHandler;
Vue.config.productionTip = false;
Vue.use(VueResource);

window.addEventListener('unhandledrejection', (e) => {
  console.warn('未处理的 promise rejection:/\n', e.reason);
  e.preventDefault();
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
