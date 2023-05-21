<template>
  <v-dialog v-model="dialog" location="bottom" max-width="700" max-height="700">
    <cart @close-cart-dialog="closeCartDialog"/>
  </v-dialog>
  <v-app-bar
    color="blue"
    density="compact"
  >
    <template v-slot:append>
      <!-- <v-btn 
        prepend-icon="mdi-logout" 
        @click="logout"
      >Logout
      </v-btn> -->
      <v-btn 
        prepend-icon="mdi-cart" 
        @click="dialog = true">
          My cart
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>

import Cart from '../components/Cart.vue'

export default {
  name: 'AppBar',
  components: {
    Cart,
  },
  data: () => ({
    dialog: false,
  }),
  methods: {
    closeCartDialog() {
        this.dialog = false;
      },
    openCartDialog() {
        this.dialog = true;
    },
    // logout() {
    //   this.$router.push('/login');
    //   localStorage.removeItem('token');
    // }
  }
}
</script>
    