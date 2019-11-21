<template>
  <v-container flex>
    <!-- ACCIONES -->
    <transition appear name="fade">
      <v-container>
        <v-row class="herramientas" justify="center" align="end">
          <v-col cols="12" sm="4" lg="4">
            <v-form>
              <v-text-field v-model="busqueda.texto" label="Search">
                <template v-slot:append-outer>
                  <v-icon @click="search">search</v-icon>
                </template>
              </v-text-field>
            </v-form>
          </v-col>
          <v-col cols="12" sm="2" lg="2">
            <v-select
              :items="categorias"
              v-model="busqueda.categorias"
              multiple
              clearable
              label="Categorías"
            >
            </v-select>
          </v-col>
          <v-col cols="12" sm="2" lg="2">
            <v-slider
              v-model="busqueda.valoracion"
              max="5"
              min="0"
              thumb-label="always"
              :thumb-size="24"
              step="1"
              ticks
              label="Valoración"
            >
            </v-slider>
          </v-col>
        </v-row>

        <v-row class="herramientas" justify="center" align="end">
          <v-col cols="12" sm="2" lg="2">
            <v-range-slider
              v-model="busqueda.precio"
              :max="maxPrice"
              :min="minPrice"
              label="Precio"
            >
              <template v-slot:prepend>
                <v-text-field
                  v-model="busqueda.precio[0]"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 50px"
                ></v-text-field>
              </template>
              <template v-slot:append>
                <v-text-field
                  v-model="busqueda.precio[1]"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 50px"
                ></v-text-field>
              </template>
            </v-range-slider>
          </v-col>

          <v-col cols="12" sm="2" lg="2">
            <v-slider
              v-model="busqueda.resenas"
              max="500"
              min="0"
              :color="colorReseñas"
              thumb-label="always"
              :thumb-size="24"
              step="5"
              label="Numero reseñas"
            >
            </v-slider>
          </v-col>
        </v-row>
      </v-container>
    </transition>

    <!-- PRODUCTOS -->
    <transition appear name="fade">
      <v-row v-if="products" justify="center">
        <v-col
          cols="12"
          sm="3"
          md="3"
          v-for="(product, _id) in hits"
          :key="_id"
        >
          <!-- AQUI IRÄ EL COMPONENTE NUEVO --->

          <v-card
            class="mx-auto producto"
            @click="showDetail(product)"
            max-width="400"
          >
            <v-img
              class="black--text align-end"
              height="200px"
              :src="getImage(product)"
            >
              <v-card-title>{{ product._source.nombreProducto }}</v-card-title>
            </v-img>
            <v-card-text class="text--primary">
              <v-container flex>
                <v-row>
                  <v-col cols="4">
                    <span>Id:</span>
                  </v-col>
                  <v-col cols="8" justify-self="start">
                    {{ product._source.idProduct }}
                  </v-col>
                </v-row>

                <v-divider class="mb-3"></v-divider>
                <v-row>
                  <v-col cols="4">
                    <span>Reseñas:</span>
                  </v-col>
                  <v-col cols="8" justify-self="start">
                    {{ product._source.numResenas }}
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="4">
                    <span>Precio:</span>
                  </v-col>
                  <v-col cols="8" justify-self="start">
                    {{ product._source.precio }}
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="4">
                    <span>Valoración:</span>
                  </v-col>
                  <v-col cols="8" justify-self="start">
                    {{ product._source.stars }}
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="4">
                    <span>Descripción:</span>
                  </v-col>
                  <v-col cols="8" justify-self="start">
                    {{ product._source.descripcion }}
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </transition>

    <!-- DIALOGO CON EL DETALLE -->
    <v-dialog v-model="showDialog">
      <v-card v-if="selectedItem">
        <v-img
          class="black--text align-end"
          height="200px"
          :src="getImage(selectedItem)"
        >
          <v-card-title>{{ selectedItem._source.nombreProducto }}</v-card-title>
        </v-img>

        <v-card-text class="text--primary">
          <v-container flex>
            <v-row>
              <v-col cols="4">
                <span>Id:</span>
              </v-col>
              <v-col cols="8" justify-self="start">
                {{ selectedItem._source.idProduct }}
              </v-col>
            </v-row>

            <v-divider class="mb-3"></v-divider>
            <v-row>
              <v-col cols="4">
                <span>Reseñas:</span>
              </v-col>
              <v-col cols="8" justify-self="start">
                {{ selectedItem._source.numResenas }}
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4">
                <span>Precio:</span>
              </v-col>
              <v-col cols="8" justify-self="start">
                {{ selectedItem._source.precio }}
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4">
                <span>Valoración:</span>
              </v-col>
              <v-col cols="8" justify-self="start">
                {{ selectedItem._source.stars }}
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4">
                <span>Descripción:</span>
              </v-col>
              <v-col cols="8" justify-self="start">
                {{ selectedItem._source.descripcion }}
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import store from "../_store";
const name = "products";

export default {
  name: "productList",
  data() {
    return {
      busqueda: {
        texto: "",
        categorias: [],
        valoracion: 3,
        precio: [0, 100],
        resenas: 5
      },
      categorias: [],
      products: [
        {
          id: "asdklj28usakjdh",
          name: "Proteina",
          valoracion: 4
        },
        {
          id: "asdkl122124usakjdh",
          name: "Galletas",
          valoracion: 5
        }
      ],
      selectedItem: null,
      showDialog: false,
      maxPrice: 200,
      minPrice: 0
    };
  },
  computed: {
    ...mapGetters(name, {
      hits: "hits",
      total: "total"
    }),
    colorReseñas() {
      if (this.busqueda.resenas < 50) return "red";
      if (this.busqueda.resenas < 200) return "orange";
      return "green";
    }
  },
  created() {
    const STORE_KEY = name;
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store);
    }
  },
  mounted() {
    this.$store.dispatch(name + "/getEntities");
  },
  methods: {
    showDetail(item) {
      this.selectedItem = item;
      this.showDialog = true;
    },
    getImage(prod) {
      if (prod._source.imageUrl) {
        return "//s1.thcdn.com/productimg/1600/1600/" + prod._source.imageUrl;
      }
      return "https://yt3.ggpht.com/a/AGF-l79djj7d-Ccsf1IXCzfapfRXyZYIhCPmX3e84w=s900-c-k-c0xffffffff-no-rj-mo";
    },
    search() {
      this.$store.dispatch(name + "/getEntitiesWithFilter", this.busqueda);
    }
  }
};
</script>
<style scoped>
.herramientas {
  margin-top: 1%;
  margin-bottom: 1%;
}
.producto {
  transition: all 0.2s ease-in-out;
  min-height: 400px;
}

.producto:hover {
  transform: translateY(-10px);
  box-shadow: 5px 5px rgba(128, 128, 128, 0.431);
}

.fade-enter-active {
  animation: fade-in 0.5s;
}
.fade-leave-active {
  animation: fade-in 0.5s reverse;
}
@keyframes fade-in {
  0% {
    transform: rotate(0) translateY(-20px);
    opacity: 0;
  }
  100% {
    transform: rotate(0) translateX(0px);
    opacity: 1;
  }
}
</style>
