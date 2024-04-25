<template>
    <div>
      <nav class="navbar is-primary">
        <div class="navbar-brand">
          <a class="navbar-item">
            <img class="logo" src="../public/roof_icon.png">
            Predictive Roofing
          </a>
          <NavigationDropDown :isOpen="isNavigationDropdownOpen" @update:isOpen="isNavigationDropdownOpen = $event"/>
        </div>
  
        <div id="main-navbar" class="navbar-menu">
          <div class="navbar-start" @click.prevent="toggleNavigationDropdown">
            <a class="navbar-item">{{ $route.meta.title }}</a>
          </div>
        </div>
  
        <div class="navbar-end">
          <UserProfileOverLay v-if="isAuthenticated" :userName="userName" :profileImgUrl="profileImgUrl" />
        </div>
      </nav>
  
      <div id="main-content">
        <router-view></router-view>
      </div>
  
      <!-- Footer -->
      <Footer />
    </div>
  </template>
  
  <script>
  import UserProfileOverLay from "@/components/UserProfileOverLay.vue";
  import NavigationDropDown from "@/components/NavigationDropDown.vue";
  import Footer from "@/components/Footer.vue";
  
  import { mapActions, mapState } from 'vuex';
  
  export default {
    computed: {
      isAuthenticated() {
        return this.$store.getters.isAuthenticated;
      }
    },
    components: {
      UserProfileOverLay,
      NavigationDropDown,
      Footer
    },
    created() {
      this.fetchUser();
    },
    data() {
      return {
        profileImgUrl: "https://cdn1.iconfinder.com/data/icons/avatar-2-2/512/Programmer-1024.png",
        isNavigationDropdownOpen: false,
      };
    },
    methods: {
      ...mapActions(['fetchUser']),
      toggleNavigationDropdown() {
        this.isNavigationDropdownOpen = !this.isNavigationDropdownOpen;
      },
    },
    computed: {
      ...mapState(['isAuthenticated', 'user']),
      userName() {
        return this.user?.username || 'Guest';
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css');
  
  /* Add your custom styles here */
  
  #main-content {
    min-height: calc(100vh - 100px); /* Adjust 100px according to your footer's height */
    padding-bottom: 100px; /* Adjust 100px according to your footer's height */
  }
  
  .Footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #333; /* Adjust as needed */
    color: #fff; /* Adjust as needed */
    padding: 20px 0; /* Adjust as needed */
  }
  </style>
  