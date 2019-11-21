<template>
  <VAppBar app dark color="warning">
    <VToolbarTitle class="white--text mr-4">
      MyProtein Viewer
    </VToolbarTitle>

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
