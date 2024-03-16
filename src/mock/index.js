import Mock from 'mockjs';

import user from './user';
import recom from './recom';
import business from './business';

Mock.mock('/user/login', 'post', user.login);
Mock.mock('/user/logout', 'post', { code: 200 });
Mock.mock('/user/info', 'get', user.info);
Mock.mock('/user/friendRecommend', 'get', user.friend);
Mock.mock('/user/recommendByHistory', 'get', recom.recommend);
Mock.mock('/user/searchForBusiness', 'get', recom.recommend2);
Mock.mock('/business/getBusinessInfo', 'get', business.Info);
Mock.mock('/business/getSuggestion', 'get', business.Suggestion);

Mock.setup({
  timeout: '300-500',
});
