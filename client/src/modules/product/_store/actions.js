import HTTP from "../../../common/http-common";

const getEntities = context => {
  HTTP.get("entities/cars")
    .then(response => {
      context.commit("CARS_FETCHED", response.data.content);
    })
    .catch(error => {
      throw error;
    });
};

const getEntityWithId = function(context, id) {
  HTTP.get("entities/cars/" + id)
    .then(response => {
      context.commit("CAR_FETCHED", response.data);
    })
    .catch(error => {
      throw error;
    });
};

const deleteEntity = function(context, id) {
  HTTP.delete("entities/cars/" + id)
    .then(() => {
      context.commit("CAR_DELETED", id);
    })
    .catch(error => {
      throw error;
    });
};

const addEntity = function(context, payload) {
  HTTP.post("entities/cars", payload)
    .then(response => {
      context.commit("CAR_ADDED", response);
    })
    .catch(error => {
      throw error;
    });
};

const updateEntity = function(context, payload) {
  HTTP.put("entities/cars/" + payload.id, payload)
    .then(response => {
      context.commit("CAR_UPDATED", response);
    })
    .catch(error => {
      throw error;
    });
};

export default {
  getEntities,
  getEntityWithId,
  deleteEntity,
  addEntity,
  updateEntity
};
