<template>
  <v-app>
    <v-layout>
      <app-bar ref="appBar"/>
      <v-main style="min-height: 920px;">
        <v-container fluid>
          <filters @changed-filters="handleChangedFilters"/>
          <v-row class="pt-6">
              <v-col v-for="article in articles" :key="article.id" cols="3" sm="6" md="4" lg="3" xl="2">
                <article-shop :article="article" @open-cart-dialog="openCartDialog" />
              </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-layout>
    <v-footer color="blue">©Javier Maximiano Solanilla</v-footer>
  </v-app>
</template>

<script>

import axios from 'axios'
import Filters from '../components/Filters.vue'
import ArticleShop from '../components/ArticleShop.vue'
import AppBar from '../components/AppBar.vue'

export default {
  name: 'HomeComponent',
  components: {
    Filters,
    ArticleShop,
    AppBar,
  },
  data: () => ({
    articles: [],
  }),
  mounted () {
    this.getArticles({})
  },
  methods: {
    getArticles(filters) {
      // const token = localStorage.getItem('token');
      const { price, order, category } = filters;
      axios
      .get('/v1/articles/', {
        // headers: {
        //     'Authorization': `Bearer ${token}`,
      // },
        params: {
          price_filter: price,
          order_filter: order,
          category_filter: category
        }  
    })
      .then(response => {
        this.articles = response.data;
    });
    },
    handleChangedFilters(filters) {
      this.getArticles(filters)
    },
    openCartDialog() {
      const childComponent = this.$refs.appBar;
      childComponent.openCartDialog();
    }

  }
}
</script>
