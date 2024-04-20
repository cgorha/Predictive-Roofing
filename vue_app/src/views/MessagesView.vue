<template>
  <section class="hero is-fullheight">
    <div class="">
      <div class="">
        <div class="columns">

          <!-- Contacts Section -->
          <div class="column">
            <div class="box">
              <h1 class="title"> Contacts </h1>
              <button class="button is-primary" @click="toggleModal">+ New Conversation</button>
              <div class="mt-4">
                <ul>
                  <!-- Loop through conversations -->
                  <template v-for="conversation in conversations" :key="conversation.id">
                    <template v-for="user in conversation.users">
                      <!-- Display contacts excluding the current user -->
                      <li class="box" style="cursor: pointer;" v-if="user.id !== $store.state.user.id" :key="user.id">
                        <div @click="setActiveConversation(conversation.id)">
                          <div>{{ user.username }}</div>
                          <div>{{ conversation.modified_at_formatted }}</div>
                        </div>
                      </li>
                    </template>
                  </template>
                </ul>
              </div>
            </div>
          </div>

          <!-- Messages Section -->
          <div class="column is-8">
            <div class="box">
              <h1 class="title"> Messages </h1>
              <div style="height: 285px; overflow-y: auto;" ref="messageContainer">
                <!-- Loop through messages -->
                <template v-for="message in activeConversation.messages" :key="message.id">
                  <!-- Primary message bubble -->
                  <div class="message is-primary" style="display: flex; align-items: flex-start; margin-bottom: 20px;"
                    v-if="message.created_by && message.created_by.id === $store.state.user?.id"
                  >
                    <div style="margin-right: 10px;">
                      <figure class="image is-64x64">
                        <img src="https://avatar.iran.liara.run/public/78" class="is-rounded">
                      </figure>
                      <p class="has-text-weight-bold">{{ message.created_at_formatted }} ago</p>
                    </div>
                    <div>
                      <p>{{ message.body }}</p>
                    </div>
                  </div>

                  <!-- Dark message bubble -->
                  <div class="message is-dark" style="display: flex; align-items: flex-start; margin-bottom: 20px;"
                    v-else
                  >
                    <div style="margin-right: 10px;">
                      <figure class="image is-64x64">
                        <img src="https://avatar.iran.liara.run/public/78" class="is-rounded">
                      </figure>
                      <p class="has-text-weight-bold">{{ message.created_at_formatted }} ago</p>
                    </div>
                    <div>
                      <p>{{ message.body }}</p>
                    </div>
                  </div>

                  <!-- Modal dialog -->


                </template>
                <ModalDialog v-if="showModal"  @message-sent="handleMessageSent" @close="toggleModal" @send="sendMessage"/>

              </div>
              <!-- Text input -->
              <div class="hero-footer" style="margin-top: 10px;">
                <form v-on:submit.prevent="submitForm">
                  <div class="section is-small" style="display: flex; flex-direction: column;">
                    <textarea v-model="body" class="input" style="height: 100px; margin-bottom: 10px;" type="text" placeholder="Type your message here"></textarea>
                    <div>
                      <button class="button is-normal is-primary ">Send</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import ModalDialog from '@/components/ModalDialog.vue';

export default {
  name: 'MessagesView',
  components: {
    ModalDialog
  },

  data() {
    return {
      conversations: [],
      activeConversation: {
        messages: []
      },
      body: '',
      showModal: false
    }
  },

  mounted() {
    this.getConversations();
  },

  methods: {

    toggleModal() {
      this.showModal = !this.showModal;
    },

    setActiveConversation(id) {
      this.activeConversation = id;
      this.getMessages();
    },

    async getConversations() {
      try {
        const response = await axios.get('/api/chat/', {
          headers: {
            'Authorization': `Token ${this.$store.state.userToken}`
          }
        });
        this.conversations = response.data;
        if (this.conversations.length) {
          this.activeConversation = this.conversations[0].id;
          this.getMessages();
        }
      } catch (error) {
        console.log(error);
      }
    },

    async getMessages() {
      try {
        const response = await axios.get(`/api/chat/${this.activeConversation}/`, {
          headers: {
            'Authorization': `Token ${this.$store.state.userToken}`
          }
        });
        this.activeConversation = response.data;
        this.scrollToBottom();
      } catch (error) {
        console.log(error);
      }
    },

    submitForm() {
      axios
        .post(`/api/chat/${this.activeConversation.id}/send/`, {
          body: this.body
        }, {
          headers: {
            'Authorization': `Token ${this.$store.state.userToken}`
          }
        })
        .then(response => {
          if (response.data && typeof response.data === 'object' && response.data.id) {
            if (response.data.created_by && response.data.created_by.id === this.$store.state.user.id) {
              if (!Array.isArray(this.activeConversation.messages)) {
                this.activeConversation.messages = [];
              }
              this.activeConversation.messages.push(response.data);
              this.scrollToBottom();
            }
          } else {
            console.error('Invalid message data received:', response.data);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    scrollToBottom() {
      this.$refs.messageContainer.scrollTop = this.$refs.messageContainer.scrollHeight;
    },

    handleMessageSent(data) {
      // Handle the message sent event
      console.log('Message sent:', data);
      // Update the view or perform any necessary actions
    },
  }
};
</script>
