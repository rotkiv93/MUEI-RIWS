import HTTP from "@/common/http-common";
import queryParser from "@/common/queryParser";

const getEntities = context => {
  HTTP.get("?q=age:45")
    .then(response => {
      console.log(response);
      //context.commit("PRODUCTS_FETCHED", response.data.content);
    })
    .catch(error => {
      throw error;
    });
};

const getEntityWithFilter = function(context, filters) {
  HTTP.get("?q=" + queryParser(filters))
    .then(response => {
      console.log(response);
      //context.commit("PRODUCTS_FETCHED", response.data);
    })
    .catch(error => {
      throw error;
    });
};

export default {
  getEntities,
  getEntityWithFilter
};
