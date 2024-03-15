import Mock from 'mockjs';

import user from './user';
import recom from './recom';

Mock.mock('/user/login', 'post', user.login);
Mock.mock('/user/logout', 'post', { code: 200 });
Mock.mock('/user/info', 'get', user.info);
Mock.mock('/user/friendRecommend', 'get', user.friend);
Mock.mock('/user/recommendByHistory', 'get', recom.recommend);
Mock.mock('/user/searchForBusiness', 'get', recom.recommend2);

Mock.setup({
  timeout: '300-500',
});
