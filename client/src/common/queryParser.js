/*
search: function() {
            var body = {
                    size: 200,
                    from: 0,
                    query: {
                        match: {
                            name: this.query
                        }
                    }
                }
 */
const basicQuery = {
  query: {
    bool: {
      must: [
        {
          multi_match: {
            query: "",
            fields: ["nombreProducto^3", "descripcion"]
          }
        },
        {
          range: {
            precio: {
              gte: 30
            }
          }
        }
      ]
    }
  }
};

export default function queryParser(filters) {
  if (filters.texto) {
    basicQuery.query.multi_match.query = filters.texto;
  }
  //   if (filters.resenas) {
  // }

  //   if (filters.texto) {
  //   }
  //   if (filters.valoracion) {
  //   }
  //   if (filters.categorias.length != 0) {
  //   }
  //   if (filters.precio[0] == 0 && filters.precio[1] == 0) {
  //   }
  return basicQuery;
}
