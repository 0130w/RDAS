import Mock from 'mockjs';

import user from './user';
import recom from './recom';

Mock.mock('/user/login', 'post', user.login);
Mock.mock('/user/logout', 'post', { code: 2000 });
Mock.mock('/user/info', 'get', user.info);
Mock.mock('/user/recommendByHistory', 'get', recom.recommend);

Mock.setup({
  timeout: '300-500',
});
