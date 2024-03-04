import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import HomeView from '../views/Home.vue'
import AddLeadView from '../views/AddLeadView.vue'
import SignUp from '../views/SignUpView.vue'
import LogIn from '../views/LogIn.vue'

const routes = [
  
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },

  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView,
    meta: {
      title: 'Dashboard',
    },
  },
  {
    path: '/leads',
    name: 'leads',
    component: () => import(/* webpackChunkName: "about" */ '../views/LeadsView.vue'),
    meta:{
      title: "Leads & Jobs"
    },
  },
  {
    path: '/messages',
    name: 'messages',
    component: () => import(/* webpackChunkName: "about" */ '../views/MessagesView.vue'),
    meta:{
      title: "Messages"
    },
  },
  {
    path: '/calendar',
    name: 'calendar',
    component: () => import(/* webpackChunkName: "about" */ '../views/CalendarView.vue'),
    meta:{
      title: "Calendar"
    },
  },
  {
    path: '/addLead',
    name: 'addLead',
    component: AddLeadView,
    meta:{
      title: "Add Lead"
    },
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import(/* webpackChunkName: "about" */ '../views/SettingsView.vue'),
    meta:{
      title: "Settings"
    },
  },
  {
    path: '/log-in',
    name: 'log-in',
    component: LogIn,
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUp,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
