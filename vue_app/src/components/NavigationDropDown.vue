<template>
    <div class="navigation-dropdown" @click="toggleDropdown" v-on:click.stop>
        <div class="dropdown" :class="{ 'is-active': dropdownActive }">
            <div class="dropdown-menu" role="menu">
                <div class="dropdown-content">
                    <router-link to="/dashboard" class="dropdown-item">Dashboard</router-link>
                    <router-link to="/leads" class="dropdown-item">Leads & Jobs</router-link>
                    <router-link to="/messages" class="dropdown-item">Messages</router-link>
                    <router-link to="/calendar" class="dropdown-item">Calendar</router-link>
                    <router-link to="/addLead" class="dropdown-item">Add Lead</router-link>
                    <router-link to="/settings" class="dropdown-item">Settings</router-link>
                    <hr class="dropdown-divider">
                    <a class="dropdown-item" @click="logout">Log Out</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NavigationDropDown',
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
            // Emit an event to synchronize state with the parent component
            this.$emit('update:isOpen', this.dropdownActive);
        }
    }
}
</script>

<style scoped>
.navigation-dropdown {
    position: relative;
    display: inline-block;
}

.navbar-item.has-cursor-pointer {
    cursor: pointer;
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
