const CARS_FETCHED = (state, messages) => {
  state.entities = messages;
};

const CAR_FETCHED = (state, message) => {
  state.entities = [
    ...state.entities.filter(element => element.id != message.id),
    message
  ];
};

const CAR_DELETED = (state, id) => {
  state.entities.forEach(function(item, index, object) {
    if (item.id == id) {
      object.splice(index, 1);
    }
  });
};

const CAR_ADDED = (state, payload) => {
  state.entities.push(payload);
};

const CAR_UPDATED = (state, payload) => {
  state.entities = [
    ...state.entities.filter(element => element.id != payload[0].id),
    payload[0]
  ];
};

export default {
  CAR_FETCHED,
  CARS_FETCHED,
  CAR_DELETED,
  CAR_ADDED,
  CAR_UPDATED
};
