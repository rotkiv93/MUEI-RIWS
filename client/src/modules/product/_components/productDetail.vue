<template>
  <v-container>
    <v-card v-if="entity">
      <v-card-title class="headline">
        Car
        <v-spacer></v-spacer>
        <v-btn @click="back()">Back</v-btn>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-layout> id: {{ entity.id }} </v-layout>

          <v-layout> brand: {{ entity.brand }} </v-layout>

          <v-layout> model: {{ entity.model }} </v-layout>

          <v-layout> color: {{ entity.color }} </v-layout>

          <v-layout> location: {{ entity.location }} </v-layout>

          <v-layout> owner: {{ entity.owner }} </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn class="yellow darken-3 white--text" @click="edit()">Edit</v-btn>
        <v-btn class="red white--text" @click="showDeleteDialog">Remove</v-btn>
      </v-card-actions>
    </v-card>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="headline darken-1 red white--text">
          Delete entity
        </v-card-title>
        <v-card-text>
          This action will be permanent
          <br />
          Are you sure you want to continue?
        </v-card-text>
        <v-card-actions>
          <v-btn @click="dialog = false">
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn @click="deleteEntity" color="red darken-1 white--text"
            >Continue <v-icon> delete </v-icon></v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import store from "../_store";
const name = "cars";

export default {
  name: "carDetail",
  data() {
    return {
      dialog: false
    };
  },
  watch: {
    $route: "mounted"
  },
  created() {
    const STORE_KEY = name;
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store);
    }
  },
  mounted() {
    this.$store.dispatch(name + "/getEntityWithId", this.$route.params.id);
  },
  computed: {
    ...mapGetters(name, {
      message: "entityWithId"
    }),
    entity() {
      return this.message(this.$route.params.id);
    }
  },
  methods: {
    edit() {
      this.$router.push({
        name: "carForm",
        params: { id: this.entity.id }
      });
    },
    back() {
      this.$router.go(-1);
    },
    showDeleteDialog() {
      this.dialog = true;
    },
    deleteEntity() {
      this.$store.dispatch(name + "/deleteEntity", this.entity.id).then(() => {
        this.dialog = false;
        this.$router.push({ name: "carList" });
      });
    }
  }
};
</script>
