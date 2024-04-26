<template>
    <div class="sidebar">
        <div class="dropdown" :class="{ 'is-active': dropdownActive }">
            <aside class="menu">
                <ul class="menu-list">
                    <li>
                        <router-link to="/dashboard" class="menu-item">Dashboard</router-link>
                    </li>
                    <li>
                        <router-link to="/leads" class="menu-item">Leads & Jobs</router-link>
                    </li>
                    <li>
                        <router-link to="/messages" class="menu-item">Messages</router-link>
                    </li>
                    <li>
                        <router-link to="/calendar" class="menu-item">Calendar</router-link>
                    </li>
                    <li>
                        <router-link to="/addLead" class="menu-item">Add Lead</router-link>
                    </li>
                    <li>
                        <router-link to="/settings" class="menu-item">Settings</router-link>
                    </li>
                    <hr class="sidebar-divider" />
                    <li>
                        <a class="menu-item" @click.prevent="logout">Log Out</a>
                    </li>
                </ul>
            </aside>
        </div>
    </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
    name: "SidebarMenu",
    props: {
        isOpen: {
            type: Boolean,
            default: false
        }
    },
    watch: {
        isOpen(newValue) {
            this.dropdownActive = newValue;
        }
    },
    data() {
        return {
            dropdownActive: false
        };
    },
    methods: {
        toggleDropdown() {
            this.dropdownActive = !this.dropdownActive;
            this.$emit('update:isOpen', this.dropdownActive);
        },
        ...mapActions(["logout"]),
    },
};
</script>

<style scoped>
.sidebar {
    background-color: #2c3e50;
    color: #fff;
    padding: 1rem;
    height: 100vh;
    width: 200px;
}

.menu-item {
    color: #fff;
    display: block;
    padding: 0.5rem 1rem;
    text-decoration: none;
}

.menu-item:hover {
    background-color: #34495e;
}

.sidebar-divider {
    border-color: #d3d3d3;
    margin: 0.5rem 0;
}
</style>