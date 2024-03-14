import Vue from 'vue';
import VueRouter from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue';
import UserLayout from '@/layouts/UserLayout.vue';
import Page from '@/views/Page.vue';

Vue.use(VueRouter);

export const constantRoutes = [
  {
    path: '/',
    redirect: '/homepage',
  },

  // 登录注册
  {
    path: '/user',
    redirect: '/user/login',
    component: UserLayout,
    hidden: true,
    children: [
      {
        path: 'login',
        name: 'Login',
        components: {
          login: () => import('@/views/user/Login.vue'),
        },
        meta: { title: '登录' },
      },
      {
        path: 'register',
        name: 'Register',
        components: {
          register: () => import('@/views/user/Register.vue'),
        },
        meta: { title: '注册' },
      },
    ],
  },

  // 404 路由缺失页面
  {
    path: '/not-found',
    component: () => import('@/views/error-pages/NotFound.vue'),
    meta: { title: '404 NotFound' },
  },
];

export const asyncRoutes = [

  {
    path: '',
    component: MainLayout,
    single: true,
    hidden: true,
    children: [
      {
        path: 'homepage',
        name: 'HomePage',
        component: Page,
        meta: { title: '首页', icon: 'file-text' },
      },
    ],
  },
  {
    path: '',
    meta: {
      title: '管理员界面', icon: 'folder', openKey: 'pages', permission: ['admin'],
    },
    component: MainLayout,
    children: [
      {
        path: 'infopannel',
        name: 'InfoPannel',
        component: () => import('@/views/admin/Analytics.vue'),
        meta: { title: '数据面板', openKey: 'pages' },
      },
    ],
  },
  {
    path: '',
    meta: {
      title: '用户界面', icon: 'folder', openKey: 'pages', permission: ['user'],
    },
    component: MainLayout,
    children: [
      {
        path: '/user/search',
        name: 'Search',
        component: () => import('@/views/user/Search.vue'),
        meta: { title: '搜索', openKey: 'pages' },
      },
      {
        path: '/user/infoChart',
        name: 'InfoChart',
        component: Page,
        meta: { title: '数据图表', openKey: 'pages' },
      },
      {
        path: '/user/friends',
        name: 'Friends',
        component: () => import('@/views/user/Friends.vue'),
        meta: { title: '好友推荐', openKey: 'pages' },
      },
    ],
  },
  {
    path: '',
    meta: {
      title: '商户界面', icon: 'folder', openKey: 'pages', permission: ['business'],
    },
    component: MainLayout,
    children: [
      {
        path: '/business/infoChart',
        name: 'InfoChart',
        component: Page,
        meta: { title: '数据图表', openKey: 'pages' },
      },
      {
        path: '/business/recommend',
        name: 'Recommend',
        component: () => import('@/views/business/Suggestion.vue'),
        meta: { title: '经营建议', openKey: 'pages' },
      },
    ],
  },

  { path: '*', redirect: '/not-found', hidden: true },
];

const createRouter = () => new VueRouter({
  mode: process.env.VUE_APP_ROUTER_MODE || 'history',
  base: process.env.BASE_URL,
  routes: constantRoutes,
});

const router = createRouter();

export function resetRouter() {
  const newRouter = createRouter();
  router.matcher = newRouter.matcher; // 重置路由
}

export default router;
