import HTTP from "@/common/http-common";
import queryParser from "@/common/queryParser";

const getEntities = context => {
  HTTP.get()
    .then(response => {
      context.commit("PRODUCTS_FETCHED", response.data.hits);
    })
    .catch(error => {
      throw error;
    });
};

const getEntitiesWithFilter = function(context, filters) {
  HTTP.post("", queryParser(filters))
    .then(response => {
      context.commit("PRODUCTS_FETCHED", response.data.hits);
    })
    .catch(error => {
      throw error;
    });
};

export default {
  getEntities,
  getEntitiesWithFilter
};
