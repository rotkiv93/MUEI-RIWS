import Vue from "vue";
import axios from "axios";

const HTTP = axios.create({
  baseURL: "http://localhost:8080/api/"
});

const onUnauthorized = () => {
  Vue.notify({
    text: "Access denied!",
    type: "error"
  });
};
const onResponseSuccess = response => response;

const onResponseFailure = err => {
  const status = err.response.status;
  // excepto cuando estemos haciendo login
  if (!err.config.url.includes("authenticate")) {
    if (status == 401 || status == 403) {
      onUnauthorized();
    }
  }
  return Promise.reject(err);
};

const onRequest = config => {
  return config;
};

HTTP.interceptors.response.use(onResponseSuccess, onResponseFailure);
HTTP.interceptors.request.use(onRequest);

export default HTTP;
