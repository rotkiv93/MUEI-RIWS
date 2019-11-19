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

export default function queryParser(filters) {
  return JSON.stringify(filters);
}
