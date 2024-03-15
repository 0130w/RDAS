import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import state from './state';
import getters from './getters';
import mutations from './mutations';
import actions from './actions';

import user from './modules/user';
import auth from './modules/auth';
import recom from './modules/recom';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    auth,
    recom,
  },

  state,
  getters,
  mutations,
  actions,

  plugins: [
    createPersistedState({
      paths: ['user.info'],
    }),
  ],
});
