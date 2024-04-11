<template>
    <div>
      <!-- Your HTML template for displaying messages and sending new messages -->
      <h1>Send SMS</h1>
      <form @submit.prevent="sendMessage" action="/messages/" method="post">
        <label for="message">Message:</label><br>
        <textarea v-model="message" id="message" name="message" rows="4" cols="50"></textarea><br>
        <label for="phone-number">Phone Number:</label><br>
        <input v-model="phoneNumber" type="text" id="phone-number" name="phone_number"><br>
        
        <input type="hidden" name="csrfmiddlewaretoken" v-model="csrfToken">
        <button type="submit">Send SMS</button>
      </form>
  
      <div v-if="messageStatus" class="message-status">{{ messageStatus }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import {mapState} from "vuex";
  
  export default {
    data() {
      return {
        message: '',
        phoneNumber: '',
        messageStatus: '',
        csrfToken: ''
      };
    },
      computed: {
          ...mapState(['userToken']),
      },
    mounted() {
      this.csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    },
    methods: {
      sendMessage() {
        const headers = {
            'Authorization': `Token ${this.userToken}`
        };
  
        axios.post('/api/messages/', {
          message: this.message,
          phone_number: this.phoneNumber
        }, { headers })
        .then(response => {
          this.messageStatus = 'SMS sent successfully';
        })
        .catch(error => {
          this.messageStatus = 'Error: ' + error.response.data;
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .message-status {
    margin-top: 10px;
    color: green;
  }
  </style>
  