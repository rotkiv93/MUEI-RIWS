import HTTP from "@/common/http-common";
import queryParser from "@/common/queryParser";

const getEntitiesWithFilter = function(context, filters) {
  return HTTP.post("", queryParser(filters))
    .then(response => {
      return context.commit("PRODUCTS_FETCHED", response.data.hits);
    })
    .catch(error => {
      throw error;
    });
};

export default {
  getEntitiesWithFilter
};
