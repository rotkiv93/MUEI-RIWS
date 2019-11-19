const entities = state => state.entities;

const entityWithId = state => id => {
  if (!id) {
    return state.entities;
  } else {
    return state.entities.filter(el => el.id == id)[0];
  }
};

export default {
  entities,
  entityWithId
};
