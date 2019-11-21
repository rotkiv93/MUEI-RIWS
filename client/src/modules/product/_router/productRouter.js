/* eslint-disable */
const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../_components/productList")
  },
  {
    path: "/products",
    name: "productList",
    component: () => import("../_components/productList")
  }
];

export default routes;
