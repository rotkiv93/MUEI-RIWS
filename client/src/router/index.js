import Vue from "vue";
import VueRouter from "vue-router";

import productRouter from "../modules/product/_router/productRouter";

Vue.use(VueRouter);

const routes = [];

const router = new VueRouter({
  mode: "history",
  routes: routes.concat(productRouter)
});

export default router;
