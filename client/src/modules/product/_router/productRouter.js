/* eslint-disable */
const routes = [
  {
    path: "/products",
    name: "productList",
    component: () =>
      import("../_components/productList")
  },
  {
    path: "/products/:id",
    name: "productDetail",
    component: () =>
      import("../_components/productDetail")
  }
];

export default routes;
