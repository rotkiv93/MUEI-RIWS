<template>
  <v-container flex>
    <!-- ACCIONES -->
    <transition appear name="fade">
      <v-container>
        <v-row class="herramientas" justify="center" align="end">
          <v-col cols="12" sm="5" lg="5">
            <v-form>
              <v-text-field v-model="busqueda.texto" label="Search">
                <template v-slot:append-outer>
                  <v-icon @click="search">search</v-icon>
                </template>
              </v-text-field>
            </v-form>
          </v-col>
          <v-col cols="12" sm="3" lg="3">
            <v-select
              :items="categorias"
              v-model="busqueda.categorias"
              multiple
              clearable
              label="Categorías"
            >
            </v-select>
          </v-col>
        </v-row>

        <v-row class="herramientas" justify="center" align="end">
          <v-col cols="12" sm="3" lg="3">
            <v-range-slider
              v-model="busqueda.precio"
              :max="maxPrice"
              :min="minPrice"
              :thumb-label="true"
              label="Precio"
            >
            </v-range-slider>
          </v-col>

          <v-col cols="12" sm="3" lg="3">
            <v-slider
              v-model="busqueda.resenas"
              max="200"
              min="0"
              :color="colorReseñas"
              thumb-label="always"
              :thumb-size="24"
              step="5"
              label="Numero reseñas"
            >
            </v-slider>
          </v-col>

          <v-col cols="12" sm="3" lg="3">
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
      </v-container>
    </transition>

    <!-- PRODUCTOS -->
    <transition appear name="fade">
      <v-row v-if="hits" justify="center">
        <v-col
          cols="12"
          sm="3"
          md="3"
          v-for="(product, _id) in hits"
          :key="_id"
        >
          <!-- VISTA DE PRODUCTOS NORMAL --->
          <productDetail v-bind:product="product"></productDetail>
        </v-col>
      </v-row>
    </transition>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import store from "../_store";
import productDetail from "./productDetail";
const name = "products";

export default {
  name: "productList",
  components: { productDetail },
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
