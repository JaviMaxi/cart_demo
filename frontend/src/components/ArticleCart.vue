<template>
  <v-card 
    variant="outlined"
    height="380"
    width="280"
  >
    <v-img
      height="220"
      width="280"
      :src="articleCart.article.file_url"
    ></v-img>
    <v-card-text>
      <p><strong>Name:</strong> {{ articleCart.article.name }}</p>
      <p><strong>Model:</strong> {{ articleCart.article.model }}</p>
      <p><strong>Price:</strong> {{ articleCart.article.price }} €</p>
      <v-row class="pt-2 pl-6">
        <units-component 
          ref="unitsComponent" 
          @update-article-cart="updateArticleCart"/>
        <v-btn 
          icon 
          variant="plain" 
          class="pt-9 pl-8" 
          @click="removeArticleCart()"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </v-row>
    </v-card-text>
  </v-card>  
</template>

<script>

import axios from 'axios'
import UnitsComponent from '../components/UnitsComponent.vue'

export default {
  name: 'ArticleCart',
  props: {
      articleCart: {
          type: Array,
          required: true
      },
  },
  components: {
      UnitsComponent,
  },
  data() {
    return {
      quantity: null
    };
  },
  mounted () {
      const childComponent = this.$refs.unitsComponent;
      childComponent.updateQuantity(this.articleCart.quantity);
  },
  methods: {
    removeArticleCart() {
      // const token = localStorage.getItem('token');
      let url = '/v1/cart-item/delete';
      
      axios
      .delete(url, {
          data: {
            article: this.articleCart.article.id,
        }
        }, {
        //   headers: {
        //     'content-type': 'multipart/form-data',
        //     'Authorization': `Bearer ${token}`,
        // }
      })
      .then(response => {
        this.$emit('update-cart');
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      });
    },
    updateArticleCart(quantity) {
      // const token = localStorage.getItem('token');
      let form_data = new FormData();
      form_data.append('article', this.articleCart.article.id);
      form_data.append('quantity', quantity);
      let url = '/v1/cart-item/update';

      axios
      .patch(url, form_data,
      {
        // headers: {
        //   'content-type': 'multipart/form-data',
        //   'Authorization': `JWT ${token}`,
        // }
      })
      .then(response => {
        this.$emit('update-cart');
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      });
    }
  }
}
</script>