import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'
import axios from "axios";
import store from './store'

axios.interceptors.response.use(
  function (response) {
    // Do something with response data
    return response;
  },
  function (error) {
    // Do something with response error
    if (
      !localStorage.token ||
      (error.response &&
        error.response.data &&
        (error.response.data.detail == "Signature has expired." ||
          error.response.data.detail == "Invalid signature."))
    ) {
      var login_redirect_path = router.app.$session.get("login_redirect_path");
      router.app.$session.destroy();
      router.app.$session.start();
      if (!login_redirect_path) {
        var current_path = router.currentRoute.fullPath;
        router.app.$session.set("login_redirect_path", current_path);
      }
      router.push("/login");
    }
    return Promise.reject(error);
  }
);

loadFonts()

createApp(App).use(store).use(router)
  .use(vuetify)
  .mount('#app')
