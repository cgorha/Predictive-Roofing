<template>
    <div class="user-profile" @click="toggleDropdown" v-on:click.stop>
        <img :src="profileImgUrl" alt="User's profile picture" />
        <span>{{ userName }}</span>
        <div class="dropdown" :class="{ 'is-active': dropdownActive }">
            <div class="dropdown-menu" role="menu">
                <div class="dropdown-content">
                    <a href="/profile" class="dropdown-item">Profile</a>
                    <a href="/settings" class="dropdown-item">Settings</a>
                    <hr class="dropdown-divider">
                    <a class="dropdown-item" @click.prevent="logout">Log Out</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
    props: {
        userName: String,
        profileImgUrl: String
    },
    data() {
        return {
            dropdownActive: false,
        };
    },
    methods: {
        toggleDropdown() {
            this.dropdownActive = !this.dropdownActive;
        },
        ...mapActions(['logout']),
    }
}
</script>

<style scoped>
.user-profile {
    padding: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
}
.user-profile img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
}
.user-profile {
    padding: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    position: relative; /* Ensures dropdown is positioned relative to this element */
}
.user-profile img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
}
.dropdown {
    position: absolute;
    width: 100%;
    top: 100%;
    left: 0;
}
.dropdown-menu {
    width: 100%;
}
.dropdown-content {
    background-color: #363636;
    color: #f5f5f5;
}
.dropdown-item {
    color: #f5f5f5;
}
.dropdown-item:hover {
    background-color: #4a4a4a;
}
.dropdown-divider {
    border-color: #555555;
}
</style>
