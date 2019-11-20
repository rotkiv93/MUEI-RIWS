const PRODUCTS_FETCHED = (state, messages) => {
  state.hits = messages.hits;
  state.total = messages.total;
};

export default {
  PRODUCTS_FETCHED
};
