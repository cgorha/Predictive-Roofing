<template>
    <div class="dashboard-container">
        <section class="welcome-section">
            <h1>Welcome Back, {{ userName }}</h1>
            <p>Here's an overview of your day:</p>
        </section>

        <section class="tasks-section">
            <h2>Your Tasks for Today</h2>
            <ul>
                <li>10:00 AM - Client meeting at <span>123 Main Street</span></li>
                <li>1:00 PM - Roof inspection at <span>456 Elm Street</span></li>
                <li>3:00 PM - Project planning session at <span>office</span></li>
            </ul>
        </section>

        <section class="map-section">
            <h2>Next Appointment Location</h2>
            <div class="google-map-container">
                <GoogleMaps :zipCode="userZipCode" :mapOptions="{ zoom: 10, center: { lat: -33.8688, lng: 151.2093 } }"/>
            </div>
        </section>
    </div>
</template>

<script>
import GoogleMaps from '../components/googleMaps.vue';
import { mapActions, mapState } from "vuex";

export default {
    name: 'App',
    components: {
        GoogleMaps
    },
    created() {
        this.fetchUser();
    },
    computed: {
        ...mapState(['user', 'isAuthenticated']),
        userName() {
            return this.user?.username || 'Guest';
        },
        userZipCode() {
            console.log("Zip code from store:", this.user?.zip_code);
            return this.user?.zip_code || '';
        },
    },
    methods: {
        ...mapActions(['fetchUser']),
    },
};
</script>

<style scoped>
.dashboard-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.welcome-section h1,
.tasks-section h2,
.map-section h2 {
    margin-bottom: 10px;
    color: #333;
}

.tasks-section ul {
    list-style: none;
    padding: 0;
}

.tasks-section li {
    background: #f2f2f2;
    margin-bottom: 8px;
    padding: 10px;
    border-radius: 4px;
}

.tasks-section span {
    font-weight: bold;
}

.google-map-container {
    height: 400px;
    margin-top: 20px;
}
</style>
