import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/Home";

import productRouter from "../modules/product/_router/productRouter";

Vue.use(VueRouter);

const routes = [{ path: "/", name: "home", component: HomeView }];

const router = new VueRouter({
  mode: "history",
  routes: routes.concat(productRouter)
});

export default router;
