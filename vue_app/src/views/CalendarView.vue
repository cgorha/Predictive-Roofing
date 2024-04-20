<template>
    <div class="calendar-container">
        <FullCalendar class="calendar" :options="calendarOptions" ref="calendar" />
        <div class="button-container">
            <button @click="openAddEventPopup">Add Event</button>
            <button @click="removeSelectedEvent">Remove Event</button>
        </div>
        <div id="eventPopup" class="event-popup" v-if="showEventPopup">
            <h2>{{ editMode ? 'Edit Event' : 'Add Event' }}</h2>
            <label for="title">Title:</label><br>
            <input type="text" id="title" v-model="eventTitle"><br>
            <label for="time">Time:</label><br>
            <VueDatePicker v-model="eventTime" :config="datePickerConfig"></VueDatePicker><br>
            <label for="description">Description:</label><br>
            <textarea id="description" v-model="eventDescription"></textarea><br><br>
            <button @click="saveEvent">{{ editMode ? 'Save Changes' : 'Add Event' }}</button>
            <button v-if="editMode" @click="deleteEvent">Delete</button>
            <button @click="closeEventPopup">Cancel</button>
        </div>
    </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import axios from 'axios';
import { mapState } from "vuex";
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

export default {
    components: {
        FullCalendar,
        VueDatePicker
    },
    data() {
        return {
            calendarOptions: {
                plugins: [dayGridPlugin],
                initialView: 'dayGridMonth',
                events: this.fetchEvents,
                eventClick: this.handleEventClick,
            },
            showEventPopup: false,
            editMode: false,
            eventTitle: '',
            eventTime: new Date(),  // Initialize with a default date
            eventDescription: '',
            selectedEventId: null
        }
    },
    computed: {
        ...mapState(['userToken']),
        datePickerConfig() {
            return {
                format: 'YYYY-MM-DD HH:mm',
                is24hr: true,
            };
        },
    },
    methods: {
        fetchEvents(fetchInfo, successCallback, failureCallback) {
            console.log("Fetching events with token:", this.userToken);
            axios.get('/api/v1/calendar/', {
                headers: { 'Authorization': `Token ${this.userToken}` }
            })
                .then(response => {
                    console.log("Events fetched successfully:", response.data);
                    successCallback(response.data);
                })
                .catch(error => {
                    console.error('Error fetching events:', error);
                    failureCallback(error);
                });
        },
        handleEventClick(info) {
            this.openEditEventPopup(info.event);
        },
        openAddEventPopup() {
            this.showEventPopup = true;
            this.editMode = false;
            this.eventTitle = '';
            this.eventTime = '';
            this.eventDescription = '';
            this.selectedEventId = null;
        },
        openEditEventPopup(event) {
            this.showEventPopup = true;
            this.editMode = true;
            this.eventTitle = event.title;
            this.eventTime = event.start.toISOString().slice(0, 16);
            this.eventDescription = event.extendedProps.description || '';
            this.selectedEventId = event.id;
        },
        closeEventPopup() {
            this.showEventPopup = false;
            this.editMode = false;
            this.selectedEventId = null;
        },
        saveEvent() {
            const eventData = {
                title: this.eventTitle,
                start: this.eventTime,
                description: this.eventDescription
            };
            console.log("Saving event:", eventData);
            const url = this.editMode ? `/api/v1/calendar/${this.selectedEventId}/` : '/api/v1/calendar/';
            const method = this.editMode ? 'patch' : 'post';
            axios({
                method: method,
                url: url,
                headers: {
                    'Authorization': `Token ${this.userToken}`
                },
                data: eventData
            }).then(() => {
                console.log("Event saved successfully");
                this.$refs.calendar.getApi().refetchEvents();
                this.closeEventPopup();
            }).catch(error => {
                console.error('Error saving event:', error.response ? error.response.data : error);
            });
        },
        deleteEvent() {
            console.log("Deleting event ID:", this.selectedEventId);
            if (!this.selectedEventId) return;
            axios.delete(`/api/v1/calendar/${this.selectedEventId}/`, {
                headers: {
                    'Authorization': `Token ${this.userToken}`
                }
            })
                .then(() => {
                    console.log("Event deleted successfully");
                    this.$refs.calendar.getApi().refetchEvents();
                    this.closeEventPopup();
                }).catch(error => {
                console.error('Error deleting event:', error.response ? error.response.data : error);
            });
        },
        removeSelectedEvent() {
            if (!this.selectedEventId) {
                alert("Please select an event to remove.");
                return;
            }
            this.deleteEvent();
        }
    }
}
</script>

<style>
.calendar-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
.calendar {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
}
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
.event-popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    z-index: 1000;
    border: 1px solid #ccc;
}
</style>
