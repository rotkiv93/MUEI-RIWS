<template>
  <v-container flex>
    <!-- ACCIONES -->
    <transition appear name="fade">
      <v-container>
        <v-row class="herramientas" justify="center" align="end">
          <v-col cols="12" sm="5" lg="5">
            <v-form>
              <v-text-field
                v-model="busqueda.texto"
                v-on:keydown.enter.prevent="search"
                label="Search"
              >
                <template v-slot:append-outer>
                  <v-icon @click="search">search</v-icon>
                </template>
              </v-text-field>
            </v-form>
          </v-col>
          <v-col cols="12" sm="3" lg="3">
            <v-select
              :items="categoriesDisp"
              v-model="busqueda.categorias"
              multiple
              clearable
              @change="search"
              label="Categorías"
            >
            </v-select>
          </v-col>

          <v-col cols="12" sm="3" lg="3">
            <v-btn-toggle v-model="viewType">
              <v-btn icon>
                <v-icon>list</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>view_carousel</v-icon>
              </v-btn>
            </v-btn-toggle>
          </v-col>
        </v-row>

        <v-row class="herramientas" justify="center" align="end">
          <v-col cols="12" sm="3" lg="3">
            <v-range-slider
              v-model="busqueda.precio"
              @change="search"
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
              @change="search"
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
              @change="search"
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
      <!-- VISTA DE CARRUSEL --->
      <v-row v-if="hits && viewType == 1" justify="center">
        <v-col
          cols="12"
          sm="3"
          md="3"
          v-for="(product, _id) in hits"
          :key="_id"
        >
          <productDetail v-bind:product="product"></productDetail>
        </v-col>
      </v-row>
      <v-row v-if="hits && viewType == 0">
        <!-- VISTA DE TABLA -->
        <v-col>
          <v-data-table
            :items="hits"
            :loading="loading"
            loading-text="Searching... Please wait"
            :headers="tableHeaders"
            hide-default-footer
          >
          </v-data-table>
        </v-col>
      </v-row>
    </transition>
    <v-row justify="center">
      <v-col>
        <div class="text-center pt-2">
          <v-pagination
            v-model="page"
            :length="length"
            :next-icon="nextIcon"
            :prev-icon="prevIcon"
            :page="page"
            :total-visible="totalVisible"
            @input="goPage($event)"
          ></v-pagination>
        </div>
      </v-col>
    </v-row>
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
      // FILTROS A APLICAR EN LA BUSQUEDA
      busqueda: {
        texto: "",
        categorias: [],
        valoracion: 3,
        precio: [0, 100],
        resenas: 5,
        from: 0,
        size: 10
      },
      categoriesDisp: ["Vegetariano", "Vegan"],
      maxPrice: 200,
      minPrice: 0,

      // TIPO DE VISTA Y TABLA
      viewType: 0,
      loading: true,
      tableHeaders: [
        { text: "Id", value: "_source.idProduct" },
        { text: "Nombre Producto", value: "_source.nombreProducto" },
        { text: "Num Reseñas", value: "_source.numResenas" },
        { text: "Precio", value: "_source.precio" },
        { text: "Valoracion", value: "_source.stars" },
        { text: "Categoria", value: "_source.categoria" }
      ],
      // Paginacion

      pageSize: 10,
      length: null,
      nextIcon: "navigate_next",
      nextIcons: ["mdi-chevron-right", "mdi-arrow-right", "mdi-menu-right"],
      prevIcon: "navigate_before",
      prevIcons: ["mdi-chevron-left", "mdi-arrow-left", "mdi-menu-left"],
      page: 1,
      totalVisible: 10
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
    this.loading = true;
    this.$store
      .dispatch(name + "/getEntitiesWithFilter", this.busqueda)
      .then(() => {
        this.loading = false;
        this.length = Math.floor(this.total.value / this.pageSize);
      });
  },
  methods: {
    search() {
      this.loading = true;
      this.$store
        .dispatch(name + "/getEntitiesWithFilter", this.busqueda)
        .then(() => {
          this.loading = false;
          this.length = Math.floor(this.total.value / this.pageSize);
        });
    },
    goPage(evt) {
      window.scrollTo({ top: 0, behavior: "smooth" });
      this.busqueda.from = evt == 1 ? 0 : (evt - 1) * this.pageSize;
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
