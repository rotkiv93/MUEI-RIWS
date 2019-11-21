<template>
  <!-- DIALOGO CON EL DETALLE -->
  <v-card v-if="producto">
    <v-img
      class="black--text align-end"
      height="200px"
      :src="getImage(producto)"
    >
      <v-card-title>{{ producto._source.nombreProducto }}</v-card-title>
    </v-img>

    <v-card-text class="text--primary">
      <v-container flex>
        <v-row>
          <v-col cols="4">
            <span>Id:</span>
          </v-col>
          <v-col cols="8" justify-self="start">
            <a :href="producto._source.itemURL" target="_blank">
              {{ producto._source.idProduct }}
            </a>
          </v-col>
        </v-row>

        <v-divider class="mb-3"></v-divider>
        <v-row>
          <v-col cols="4">
            <span>Reseñas:</span>
          </v-col>
          <v-col cols="8" justify-self="start">
            {{ producto._source.numResenas }}
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <span>Precio:</span>
          </v-col>
          <v-col cols="8" justify-self="start">
            {{ producto._source.precio }}
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <span>Valoración:</span>
          </v-col>
          <v-col cols="8" justify-self="start">
            {{ producto._source.stars }}
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <span>Descripción:</span>
          </v-col>
          <v-col cols="8" justify-self="start">
            {{ producto._source.descripcion }}
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ["producto"],
  data() {
    return {};
  },
  methods: {
    getImage(prod) {
      if (prod._source.imageUrl) {
        return "//s1.thcdn.com/productimg/1600/1600/" + prod._source.imageUrl;
      }
      return "https://yt3.ggpht.com/a/AGF-l79djj7d-Ccsf1IXCzfapfRXyZYIhCPmX3e84w=s900-c-k-c0xffffffff-no-rj-mo";
    }
  }
};
</script>

<style></style>
