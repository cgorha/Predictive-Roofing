import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: DashboardView
  },
  {
    path: '/leads',
    name: 'leads',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/LeadsView.vue')
  },
  {
    path: '/messages',
    name: 'messages',
    component: () => import(/* webpackChunkName: "about" */ '../views/MessagesView.vue')
  },
  {
    path: '/calendar',
    name: 'calendar',
    component: () => import(/* webpackChunkName: "about" */ '../views/CalendarView.vue')
  },
  {
    path: '/addLead',
    name: 'addLead',
    component: () => import(/* webpackChunkName: "about" */ '../views/AddLeadView.vue')
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import(/* webpackChunkName: "about" */ '../views/SettingsView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "about" */ '../views/LoginView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
