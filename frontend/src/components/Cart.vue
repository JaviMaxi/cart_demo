<template>
  <v-card>
    <v-card-title>
      <span class="headline">My cart</span>
      <v-btn 
        icon @click="closeCartDialog" 
        size="small" 
        variant="plain" 
        class="float-right"
      ><v-icon>mdi-close</v-icon></v-btn>
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>   
      <v-divider></v-divider>
      <v-container>
        <v-row 
          class="pt-6 scrollable-row" 
          wrap
        >
          <v-col 
            v-for="article in articles" 
            :key="article.id" 
            cols="6" 
            sm="6" 
            md="6" 
            lg="6" 
            xl="6"
          >
            <article-cart :articleCart="article" @update-cart="updateCart"/>
          </v-col>
        </v-row>
      </v-container>
      <v-divider></v-divider>
      <p class="font-weight-black pt-4 pl-3">
        TOTAL: {{ total }} €
      </p>
    </v-card-text>
  </v-card>
</template>

<style>
  .scrollable-row {
    overflow-x: auto;
    white-space: nowrap;
    height: 550px
  }
</style>

<script>

import ArticleCart from '../components/ArticleCart.vue'
import axios from 'axios'

export default {
  name: 'CartComponent',
  components: {
    ArticleCart,
  },
  data: () => ({
    dialog: false,
    articles: [],
    total: null,
  }),
  mounted () {
    this.getArticlesCart()
  },
  methods: {
    closeCartDialog() {
        this.$emit('close-cart-dialog');
    },
    getArticlesCart() {
      // const token = localStorage.getItem('token');
      axios
      .get('/v1/cart/', {
        // headers: {
        //   'content-type': 'multipart/form-data',
        //   'Authorization': `Bearer ${token}`,
        // }
      })
      .then(response => {
        this.articles = response.data[0].items;
        this.total = response.data[0].total
      });
    },
    updateCart() {
      this.getArticlesCart();
    }
  }
}
</script>