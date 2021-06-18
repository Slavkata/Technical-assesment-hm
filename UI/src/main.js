import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
//import "./assets/style.css"

Vue.config.productionTip = false

Vue.prototype.$api = axios.create({
  timeout: 10000,
  withCredentials: true
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
