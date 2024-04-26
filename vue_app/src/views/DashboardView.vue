<template>
    <div class="dashboard-container">
        <section class="welcome-section">
            <h1>Welcome back to Predictive Roofing, <strong>{{ userName }}</strong></h1>
        </section>

        <section class="tasks-section">
            <h2>Your Tasks for Today</h2>
            <div class="task-cards">
                <div class="task-card" v-for="task in calendarEvents" :key="task.id">
                    <div class="task-time">{{ formatDate(task.start) }}</div>
                    <div class="task-desc">{{ task.title }}</div>
                    <div class="task-location">{{ task.description }}</div>
                </div>
            </div>
        </section>

        <section class="map-section">
            <h1><strong>Hail Swath and Canvassing Record:</strong></h1>
            <p>Click a location that you have already visited to drop a pin.</p>
            <div class="google-map-container">
                <GoogleMaps :zipCode="userZipCode" :mapOptions="{ zoom: 10, center: { lat: -33.8688, lng: 151.2093 } }"/>
            </div>
        </section>
    </div>
</template>

<script>
import GoogleMaps from '../components/googleMaps.vue';
import axios from 'axios';
import { mapActions, mapState } from "vuex";

export default {
    name: 'Dashboard',
    components: {
        GoogleMaps
    },
    data() {
        return {
            calendarEvents: []
        };
    },
    computed: {
        ...mapState({
            userName: state => state.user.username || 'Guest',
            userZipCode: state => state.user.zip_code || '',
            userToken: state => state.userToken
        }),

    },
    created() {
        this.fetchUser().then(() => {
            if (this.userToken) {
                this.fetchCalendarEvents();
            } else {
                console.log("Token not available after fetchUser");
            }
        });
    },
    methods: {
        ...mapActions(['fetchUser']),
        async fetchCalendarEvents() {
            console.log("Attempting to fetch calendar events with token:", this.userToken);
            if (!this.userToken) {
                console.error("No token available for fetching calendar events.");
                return;
            }
            try {
                const response = await axios.get('/api/v1/calendar/', {
                    headers: { 'Authorization': `Token ${this.userToken}` }
                });
                this.calendarEvents = response.data;
                console.log("Calendar events fetched:", this.calendarEvents);
            } catch (error) {
                console.error('Failed to fetch calendar events:', error);
            }
        },
        formatDate(value) {
            if (!value) return 'No time provided';
            const date = new Date(value);
            return date.toLocaleString('en-US', {
                year: 'numeric', month: 'long', day: 'numeric',
                hour: '2-digit', minute: '2-digit', hour12: true,
                timeZoneName: 'short'
            });
        }
    }
};
</script>


<style scoped>
.dashboard-container {
    max-width: 960px;
    margin: 20px auto;
    background: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.welcome-section h1 {
    color: #4a4a4a;
    font-size: 24px;
}

.tasks-section h2, .map-section h1 {
    color: #363636;
    font-size: 20px;
    margin-bottom: 15px;
}

.task-card {
    background: #fff;
    border-left: 5px solid #3273dc;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.google-map-container {
    height: 400px;
    border-radius: 8px;
    overflow: hidden;
}
</style>
