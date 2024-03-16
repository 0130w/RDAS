import {
  searchForBusiness, recommendByHistory,
} from '@/api/search';

const state = {
  businesses: [],
};

const mutations = {
  SET_USER_BUSINESSES(state, businesses) {
    state.businesses = businesses;
  },
};

const actions = {

  async searchForBusiness({ commit }, {
    latitude,
    longitude,
    city,
    choice,
    options,
  }) {
    const { data } = await searchForBusiness({
      latitude,
      longitude,
      city,
      choice,
      options,
    });
    commit('SET_USER_BUSINESSES', data.businesses);
    return data;
  },

  async recommendByHistory({ commit }) {
    const { data } = await recommendByHistory();
    commit('SET_USER_BUSINESSES', data.businesses);
    return data;
  },
};

export default {
  state,
  mutations,
  actions,
};
