import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  online: navigator.onLine
};

const store = new Vuex.Store({
  state
});

export default store;
