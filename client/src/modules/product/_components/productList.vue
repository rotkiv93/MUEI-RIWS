<template>
  <v-container flex>
    <!-- ACCIONES -->
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
          v-model="busqueda.rango"
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

    <!-- PRODUCTOS -->
    <v-row v-if="products" justify="center">
      <v-col
        cols="12"
        sm="3"
        md="3"
        v-for="(product, id) in products"
        :key="id"
      >
        <!-- AQUI IRÄ EL COMPONENTE NUEVO --->
        <v-card class="producto" @click="showDetail(product)">
          <v-card-title> {{ product.name }} - {{ product.id }} </v-card-title>
          <v-card-text>
            {{ product.valoracion }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- DIALOGO CON EL DETALLE -->
    <v-dialog></v-dialog>
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
      search: "",
      busqueda: { texto: "", categorias: [], rango: 3 },
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
      showDialog: false
    };
  },
  computed: {
    ...mapGetters(name, {
      messages: "entities"
    })
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
}

.producto:hover {
  transform: translateY(-10px);
  box-shadow: 5px 5px rgba(128, 128, 128, 0.431);
}
</style>