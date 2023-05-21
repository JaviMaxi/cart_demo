import { createStore } from 'vuex';

const store =  createStore({
  state() {
    return {
      isAuthenticated: false
    }
    
  },
  mutations: {
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    }
  },
  actions: {
    setAuthentication({ commit }, isAuthenticated) {
      console.log("Entra aquiiiiiii", isAuthenticated)
      commit('setAuthentication', isAuthenticated);
    }
  },
  getters: {
    isAuthenticated(state) {
      console.log("El estado es", state.isAuthenticated)
      return state.isAuthenticated;
    }
  }
});

export default store;