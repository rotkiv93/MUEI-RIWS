<template>
  <v-app>
    <MenuBar>
      <!-- -->
    </MenuBar>

    <v-content>
      <router-view class="content">
        <!-- -->
      </router-view>
    </v-content>
  </v-app>
</template>

<script>
import MenuBar from "./components/MenuBar";

export default {
  name: "App",
  components: {
    MenuBar
  },
  data() {
    return {
      //
    };
  }
};
</script>
