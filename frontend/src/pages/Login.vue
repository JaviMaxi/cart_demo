<template>
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6">
          <v-card>
            <v-card-title class="text-center">
              <h2 class="headline mb-0">Login</h2>
            </v-card-title>
            <v-card-text>
              <v-form @submit.prevent="login">
                <v-text-field v-model="username" label="Username" :rules="emptyField" required></v-text-field>
                <v-text-field v-model="password" label="Password" type="password" :rules="emptyField" required></v-text-field>
                <v-alert v-if="loginError" type="error" class="login-alert">
                  Usuario o contraseña incorrectos.
                </v-alert>
                <v-btn type="submit" color="blue" block>Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
          
        </v-col>
      </v-row>
    </v-container>
  </template>
<script>

import axios from 'axios'
import { mapActions } from 'vuex';

export default {
  name: 'LoginComponent',
  data() {
    return {
      username: '',
      password: '',
      loginError: false,
      emptyField: [
        value => !!value || 'This field is required'
      ],
    };
  },
  methods: {
    ...mapActions(['setAuthentication']),
    login() {
        let url = '/v1/token/';
        let form_data = new FormData();
        form_data.append('username', this.username);
        form_data.append('password', this.password);
        
        axios
        .post(url, form_data)
        .then(response => {
          this.loginError = false;
            localStorage.setItem('token', response.data.access);
            this.setAuthentication(true);
            this.$router.push('/home');
        })
        .catch(error => {
            this.loginError = true;
            console.log(error);
        });
        },
  },
}
</script>

<style scoped>

.v-card {
  max-width: 400px;
  margin: auto
}
.v-container {
  height: 100vh;
  display: flex;
  align-items: center;
}

.text-center {
  text-align: center;
}

.login-alert {
  padding: 6px;
    margin-top: 5px;
    margin-bottom: 5px;
}

</style>