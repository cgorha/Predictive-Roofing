import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).use(router).mount('#app')

const companyName = 'Predictive Roofing'; 

router.beforeEach((to, from, next) => {
  const pageTitle = to.meta.title ? `${companyName} | ${to.meta.title}` : companyName;
  document.title = pageTitle;  
  next();
  });

window.initMap = function() {
  console.log('Map initialized');
};