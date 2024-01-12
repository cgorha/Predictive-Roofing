import Vue from 'vue';
import Router from 'vue-router';
import HomePage from './components/HomePage.vue';
import HelloWorld from './components/HelloWorld.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
    path: '/hello',
    name: 'hello',
    component: HelloWorld
    },
  ]
});
