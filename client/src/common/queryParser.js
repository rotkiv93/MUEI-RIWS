var bodybuilder = require("bodybuilder");
let basicQuery = [];

export default function queryParser(filters) {
  basicQuery = [];
  if (filters != null) {
    // Filtro por nombre y descripcion
    if (filters.texto != null && filters.texto != "") {
      basicQuery.push({
        type: "orQuery",
        function: "match",
        field: "nombreProducto",
        input: filters.texto
      });
      basicQuery.push({
        type: "orQuery",
        function: "match",
        field: "descripcion",
        input: filters.texto
      });
    }
    // Filtro por rango de precios
    if (filters.precio != null) {
      basicQuery.push({
        type: "andQuery",
        function: "range",
        field: "precio",
        input: { gte: filters.precio[0], lte: filters.precio[1] }
      });
    }
    // Filtro por valoracion
    if (filters.valoracion != null) {
      basicQuery.push({
        type: "andQuery",
        function: "range",
        field: "stars",
        input: { gte: filters.valoracion, boost: 2 }
      });
    }

    // Filtro por numero de reseñas
    if (filters.resenas != null) {
      basicQuery.push({
        type: "andQuery",
        function: "range",
        field: "numResenas",
        input: { gte: filters.resenas }
      });
    }

    // Filtro por categorías
    if (filters.categorias.length != 0) {
      filters.categorias.forEach(categoria => {
        basicQuery.push({
          type: "andQuery",
          function: "match",
          field: "categoria",
          input: categoria
        });
      });
    }

    const query = bodybuilder();
    basicQuery.forEach(element => {
      query[element.type](element.function, element.field, element.input);
    });

    // Pagination
    query.from(filters.from).size(filters.size);

    // Ordenacion
    if (filters.ordenacion) {
      query.sort(
        Object.keys(filters.ordenacion.value)[0],
        filters.ordenacion.value[Object.keys(filters.ordenacion.value)[0]]
      );
    }
    return query.build();
  }
}
