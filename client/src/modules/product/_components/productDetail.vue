<template>
  <v-container v-if="product">
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
            <v-col cols="12">
              <span>Reseñas: {{ product._source.numResenas }} </span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <span>Precio: {{ product._source.precio }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <span>Valoración: {{ product._source.stars }} </span>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>

    <!-- DIALOGO CON EL DETALLE -->
    <v-dialog v-model="showDialog">
      <v-card v-if="product">
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
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: "carDetail",
  props: ["product"],
  data() {
    return {
      showDialog: false
    };
  },
  methods: {
    showDetail() {
      this.showDialog = true;
    },
    getImage(prod) {
      if (prod._source.imageUrl) {
        return "//s1.thcdn.com/productimg/1600/1600/" + prod._source.imageUrl;
      }
      return "https://yt3.ggpht.com/a/AGF-l79djj7d-Ccsf1IXCzfapfRXyZYIhCPmX3e84w=s900-c-k-c0xffffffff-no-rj-mo";
    }
  }
};
</script>
<style scoped>
.producto {
  transition: all 0.2s ease-in-out;
  min-height: 400px;
}

.producto:hover {
  transform: translateY(-10px);
  box-shadow: 5px 5px rgba(128, 128, 128, 0.431);
}
</style>
