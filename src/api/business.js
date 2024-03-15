/**
 * 商户相关接口
 */

import request from '@/plugins/axios';

export function getBusinessInfo(params) {
  return request({
    url: '/business/getBusinessInfo',
    method: 'get',
    params,
  });
}

export function getSuggestion(params) {
  return request({
    url: '/business/getSuggestion',
    method: 'get',
    params,
  });
}
