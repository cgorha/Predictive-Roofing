<template>
  <div class="calendar-container">
    <FullCalendar class="calendar"
      :options="calendarOptions"
      ref="calendar"
    />
    <div class="button-container">
        <button @click="openAddEventPopup">Add Event</button>
        <button @click="removeSelectedEvent">Remove Event</button>
    </div>
    <div id="eventPopup" class="event-popup" v-if="showEventPopup">
      <h2>{{ editMode ? 'Edit Event' : 'Add Event' }}</h2>
      <label for="title">Title:</label><br>
      <input type="text" id="title" v-model="eventTitle"><br>
      <label for="time">Time:</label><br>
      <input type="text" id="time" v-model="eventTime"><br>
      <label for="description">Description:</label><br>
      <textarea id="description" v-model="eventDescription"></textarea><br><br>
      <button @click="saveEvent">{{ editMode ? 'Save' : 'Add' }}</button>
      <button v-if="editMode" @click="deleteEvent">Delete</button>
      <button @click="closeEventPopup">Cancel</button>
    </div>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'

export default {
  components: {
    FullCalendar
  },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin],
        initialView: 'dayGridMonth',
        events: [
            { id: '1', title: 'Event 1', start: '2024-04-04', description: 'Description for Event 1' },
            { id: '2', title: 'Event 2', start: '2024-04-08', description: 'Description for Event 2' },
            { id: '3', title: 'Event 3', start: '2024-04-10', description: 'Description for Event 3' }
        ],
        eventClick: this.openEditEventPopup
      },
      showEventPopup: false,
      editMode: false,
      eventTitle: '',
      eventTime: '',
      eventDescription: '',
      selectedEventId: null
    }
  },
  methods: {
    openAddEventPopup() {
      this.showEventPopup = true;
      this.editMode = false;
      this.eventTitle = '';
      this.eventTime = '';
      this.eventDescription = '';
    },
    openEditEventPopup(info) {
      this.showEventPopup = true;
      this.editMode = true;
      this.eventTitle = info.event.title;
      this.eventTime = info.event.start;
      this.eventDescription = info.event.extendedProps.description || '';
      this.selectedEventId = info.event.id;
    },
    closeEventPopup() {
      this.showEventPopup = false;
      this.editMode = false;
      this.selectedEventId = null;
    },
    saveEvent() {
      const calendarApi = this.$refs.calendar.getApi();
      if (this.editMode) {
        const event = calendarApi.getEventById(this.selectedEventId);
        event.setProp('title', this.eventTitle);
        event.setStart(this.eventTime);
        event.setExtendedProp('description', this.eventDescription);
      } else {
        calendarApi.addEvent({
          title: this.eventTitle,
          start: this.eventTime,
          allDay: true,
          description: this.eventDescription
        });
      }
      this.closeEventPopup();
    },
    deleteEvent() {
      const calendarApi = this.$refs.calendar.getApi();
      const event = calendarApi.getEventById(this.selectedEventId);
      if (event) {
        event.remove();
      }
      this.closeEventPopup();
    },
    removeSelectedEvent() {
      if (this.selectedEventId) {
        this.deleteEvent();
      } else {
        alert("Please select an event to remove.");
      }
    }
  }
}
</script>

<style>
 .calendar-container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh; /* Make the container full height of the viewport */

}
.calendar {
  width: 100%;
  max-width: 800px; /* Set a maximum width for the calendar */
  margin: 0 auto; /* Center the calendar horizontally */
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