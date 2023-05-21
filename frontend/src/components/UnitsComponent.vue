<template>
  <div>
    <v-row align="center">
      <v-btn icon @click="decrementQuantity" size="small" color="blue">
        <v-icon>mdi-minus</v-icon>
      </v-btn>
      <v-col cols="auto">
        <v-text-field
          v-model="quantity"
          outlined
          dense
          class="small-text-field pt-4"
          @update:modelValue="updateCart()"
        ></v-text-field>
      </v-col>

      <v-btn icon @click="incrementQuantity" size="small" color="blue">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-row>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      quantity: 1
    };
  },
  methods: {
    incrementQuantity() {
      this.quantity++;
      this.updateCart();
    },
    decrementQuantity() {
      if (this.quantity > 1) {
        this.quantity--;
      }
      this.updateCart();
    },
    addArticleCart() {
      this.$emit('add-article-cart', this.quantity);
    },
    updateQuantity(newQuantity) {
      this.quantity = newQuantity;
    },
    updateCart() {
      this.$emit('update-article-cart', this.quantity);
    }
  }
  };  
</script>
  
<style scoped>
  .small-text-field {
    width: 50px; 
  }
</style>