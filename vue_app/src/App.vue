<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <a class="navbar-item">
          <img class="logo" src="../public/logo.png">
          Predictive Roofing
        </a>
        
        
      </div>

      <div id="main-navbar" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">{{ $route.meta.title }}</a>
        </div>
      </div>
    </nav>

    <!-- Columns -->
    <div class="columns">
      <!-- Sidebar -->
      <div class="column is-2">
        <aside class="menu">
          <p class="menu-label">
            Overview
          </p>
          <ul class="menu-list">
            <li><router-link to="/dashboard" class ="menu-item">Dashboard</router-link></li>
            <li><router-link to="/leads" class ="menu-item">Leads & Jobs</router-link></li>
            <li><router-link to="/messages" class ="menu-item">Messages</router-link></li>
            <li><router-link to="/calendar" class ="menu-item">Calendar</router-link></li>
            <li><router-link to="/addLead" class ="menu-item">Add Lead</router-link></li>
            <div class="last-menu-item">
            <li><router-link to="/settings">Settings</router-link></li>
            <li>
              <form @submit.prevent="logout">
                <button type="submit" class="button is-danger ">Log Out</button>
              </form>
            </li>
            </div>
          </ul>
        </aside>
      </div>

      <!-- Main Content -->
      <div class="column">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      // Implement your logout logic here
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
/* You can include Bulma styles specifically for this component */
@import url('https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css');

.menu-item {
  margin-bottom: 1.0rem; /* Adjust the margin as needed */
}

.last-menu-item{
  margin-top: 31.0rem;
}



</style>
