<template>
    <div>
        <nav class="navbar is-dark">
            <div class="navbar-brand">
                <a class="navbar-item" >
                    <img class="logo" src="../public/logo.png">
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
        <router-view></router-view>
    </div>
    <Footer />
</template>

<script>

import UserProfileOverLay from "@/components/UserProfileOverLay.vue";
import NavigationDropDown from "@/components/NavigationDropDown.vue";
import Footer from "@/components/Footer.vue";

import {mapActions, mapState} from 'vuex';

export default {
    computed:{
        isAuthenticated(){
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

.menu-item {
  margin-bottom: 1.0rem;
}

.last-menu-item{
  margin-top: 31.0rem;
}



</style>
