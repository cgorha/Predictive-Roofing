<template>
    <div>
      <nav class="navbar is-primary">
            <div class="navbar-brand">
              <router-link to="/" class="navbar-item predictive-roof-font ml-4">Predictive Roofing</router-link>
            </div>

            <div id="main-navbar" class="navbar-menu">
                <div class="navbar-start">
                    <a class="navbar-item">{{ $route.meta.title }}</a>
                </div>
            </div>

            <div class="navbar-end">
                <UserProfileOverLay
                    v-if="isAuthenticated"
                    :userName="userName"
                    :profileImgUrl="profileImgUrl"
                />
            </div>
        </nav>

        <div class="columns is-gapless main-container" style="display: flex;">
            <!-- Sidebar -->
            <div class="sidebar" v-if="isAuthenticated">
                <NavigationDropDown v-if="isAuthenticated" :isOpen="true" />
            </div>

            <!-- Main Content -->
            <div class="main-content">
                <div id="main-content">
                    <router-view></router-view>
                </div>
            </div>
        </div>
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

.main-container {
    display: flex;
    width: 100%;
}

.sidebar {
    flex: 0 0 200px;
    height: 100vh;
    background-color: #2c3e50;
    color: white;
    padding: 1rem;
}

.main-content {
    flex-grow: 1;
    min-height: calc(100vh - 100px);
    padding: 0 20px;
}

.Footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #333;
    color: #fff;
    padding: 20px 0;
}

.predictive-roof-font{
  font-size: larger;
}

</style>