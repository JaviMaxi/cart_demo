<template>
  <v-card 
    variant="outlined"
    height="340"
    width="280"
  >
    <v-img
      height="220"
      width="280"
      :src="article.file_url"
    ></v-img>
    <v-card-text>
    <p><strong>Name:</strong> {{ article.name }}</p>
    <p><strong>Model:</strong> {{ article.model }}</p>
    <p><strong>Price:</strong> {{ article.price }} €</p>
    <v-row class="pt-2 pl-6 d-flex justify-end">
        <v-btn 
          icon variant="plain"  
          @click="addArticleCart"
        >
          <v-icon>mdi-cart</v-icon>
        </v-btn>
    </v-row>
    </v-card-text>
  </v-card>  
</template>

<script>

import axios from 'axios'

export default {
  name: 'ArticleComponent',
  props: {
      article: {
          type: String,
          required: true
      },
  },
  data() {
    return {
      
    };
  },
  methods: {
    addArticleCart() {
      // const token = localStorage.getItem('token');
      let form_data = new FormData();
      form_data.append('article', this.article.id);
      let url = '/v1/cart-item/add';
        
      axios
      .post(url, form_data, {
        // headers: {
        //   'content-type': 'multipart/form-data',
        //   'Authorization': `Bearer ${token}`,
        // }
      })
      .then(response => {
        console.log(response)
        this.$emit("open-cart-dialog")
      })
      .catch(error => {
        console.log(error)
      });
    }
  }
}
</script>