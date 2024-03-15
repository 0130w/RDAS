import axios from 'axios';
import Message from 'ant-design-vue/es/message'; // 引入消息组件
import { getToken, removeToken } from '@/utils/token'; // 引入 token 相关的工具函数
import responseHandler from '@/utils/response-handler'; // 引入响应处理器

// 定义全局错误处理器
const errorHandler = (error) => {
  // 解构出错误响应对象中的状态码和状态信息
  const { status = 'default', statusText = '错误信息' } = error.response;
  // 使用响应处理器处理错误
  responseHandler[status](status, statusText);

  return Promise.reject(error);
};

// 创建 axios 实例
const service = axios.create({
  baseURL: process.env.VUE_APP_REQUEST_BASE_URL, // 设置请求的基本 URL
  timeout: 20000, // 设置请求超时时间
  responseType: 'json', // 设置响应数据类型
  withCredentials: true, // 在跨域请求时是否携带凭证
});

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    // 获取 token
    const token = getToken();
    // 如果存在 token，则在请求头中添加 Authorization 字段
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  errorHandler, // 请求拦截器的错误处理
);

// 响应拦截器
service.interceptors.response.use(
  (response) => {
    // 解构响应对象中的数据
    const { data } = response;
    // 解构出数据中的状态码和消息
    const { code, message = '接口异常' } = data;
    // 如果状态码不为 2000，则显示警告消息
    if (code !== 200) {
      Message.warning(message);

      // 如果状态码为 4018，表示未授权，则移除 token 并刷新页面
      if (code === 400) {
        removeToken();
        window.location.reload();
      }

      return Promise.reject(data); // 返回 Promise.reject 以便后续处理
    }
    return data; // 返回数据
  },
  errorHandler, // 响应拦截器的错误处理
);

export default service; // 导出 axios 实例
