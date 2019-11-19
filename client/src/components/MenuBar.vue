<template>
  <VAppBar app dark color="primary">
    <router-link to="/">
      <VToolbarTitle class="white--text mr-4">
        MyProtein Viewer
      </VToolbarTitle>
    </router-link>

    <VSpacer><!-- --></VSpacer>

    <VToolbarItems>
      <VBtn :to="{ name: 'productList' }" text>
        Products
      </VBtn>
    </VToolbarItems>
  </VAppBar>
</template>

<script>
export default {
  name: "MenuBar"
};
</script>
