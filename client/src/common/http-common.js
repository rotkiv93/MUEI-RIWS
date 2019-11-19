import Vue from "vue";
import axios from "axios";

// RANGOS SON :
//count:[1 TO 5]
/**
 * 
 * Dates before 2012
 * date:{* TO 2012-01-01}
 https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html
 */

const HTTP = axios.create({
  baseURL: "http://localhost:9200/company/_search"
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
