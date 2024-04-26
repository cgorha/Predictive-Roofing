import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome' 

library.add(fas); 

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App);

app.component('font-awesome-icon', FontAwesomeIcon); // Register the component

app.use(store);
app.use(router);

app.mount('#app');

const companyName = 'Predictive Roofing'; 

router.beforeEach((to, from, next) => {
  const pageTitle = to.meta.title ? `${companyName} | ${to.meta.title}` : companyName;
  document.title = pageTitle;  
  next();
  });

window.initMap = function() {
  console.log('Map initialized');
};