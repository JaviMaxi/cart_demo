<template> 
  <v-row>
    <v-col cols="4">
      <v-card height="140px">
        <v-card-item>
          <v-card-tittle>Price</v-card-tittle>
        </v-card-item>
        <v-card-text>
          <v-range-slider
              v-model="slider"
              step="50"
              :max="2200"
              thumb-label="always"
              track-fill-color="blue"
              class="pt-5"
              @end="handleChangedFilters()"
          ></v-range-slider>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="4">
      <v-card height="140px">
        <v-card-item>
          <v-card-tittle>Categories</v-card-tittle>
        </v-card-item>
        <v-card-text>
          <v-select
              v-model="select"
              :items="categories"
              item-title="name"
              item-value="id"
              clearable
              persistent-hint
              return-object
              single-line
              @update:modelValue="handleChangedFilters()"
          ></v-select>
        </v-card-text>
      </v-card>  
    </v-col>
    <v-col cols="4">
      <v-card height="140px">
          <v-card-item>
            <v-card-tittle>Order by</v-card-tittle>
          </v-card-item>
          <v-card-text>
            <v-btn-toggle
              v-model="order"
              rounded="0"
              color="blue"
              group
              class="responsive-btn-toggle"
              @click="handleChangedFilters()"
            >
              <v-btn value="-price">
                Highest price
              </v-btn>
              <v-btn value="price">
                Lowest price
              </v-btn>
              <v-btn value="-id">
                Most recent
              </v-btn>
            </v-btn-toggle>
          </v-card-text>
      </v-card>  
    </v-col>
  </v-row>
</template>

<script>

import axios from 'axios'

export default {
  name: 'CoreFiltro',

  data: () => ({
    slider: [0, 2200],
    select: null,
    categories: [],
    order: null,
  }),
  mounted () {
    // const token = localStorage.getItem('token');
    axios
    .get('/v1/categories/', {
      // headers: {
      //   'content-type': 'multipart/form-data',
      //   'Authorization': `Bearer ${token}`,
      // }
    })
    .then(response => {
      this.categories = response.data
    })
  },
  methods: {
    handleChangedFilters() {
      const filters = {
        category: (this.select) ? this.select.id : null , 
        price: [this.slider[0], this.slider[1]], 
        order: this.order
      }
      this.$emit('changed-filters', filters);
    }
  }
}
</script>

<style scoped>
  .responsive-btn-toggle {
    display: flex;
    flex-wrap: wrap;
  }
</style>

