/**
 * 搜索相关接口
 */

import request from '@/plugins/axios';

export function searchForBusiness(params) {
  return request({
    url: '/user/searchForBusiness',
    method: 'get',
    params,
  });
}

export function recommendByHistory(params) {
  return request({
    url: '/user/recommendByHistory',
    method: 'get',
    params,
  });
}
