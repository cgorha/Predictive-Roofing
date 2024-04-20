<template>
    <div class="modal is-active">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">New Conversation</p>
                <button class="delete" aria-label="close" @click="closeModal"></button>
            </header>
            <section class="modal-card-body">
                <form @submit.prevent="sendMessage">
                    <div class="field">
                        <label class="label" for="recipient">Recipient:</label>
                        <div class="control">
                            <input class="input" type="text" id="recipient" v-model="recipientName" required>
                        </div>
                    </div>
                    <div class="field">
                        <label class="label" for="message">Message:</label>
                        <div class="control">
                            <textarea class="textarea" id="message" v-model="messageBody" required></textarea>
                        </div>
                    </div>
                    <div class="field is-grouped is-grouped-centered">
                        <div class="control">
                            <button class="button is-primary" type="submit">Send</button>
                        </div>
                        <div class="control">
                            <button class="button" @click="closeModal">Cancel</button>
                        </div>
                    </div>
                </form>
            </section>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { mapState } from "vuex";

export default {
    computed: {
        ...mapState(['userToken']),  // Correctly map the userToken from Vuex
    },
    data() {
        return {
            recipientName: '',
            messageBody: ''
        };
    },
    methods: {
        sendMessage() {
            console.log('Sending data:', {
                recipient: this.recipientName,
                body: this.messageBody
            });

            axios.post(`/api/chat/send/`, {
                recipient: this.recipientName,
                body: this.messageBody
            }, {
                headers: {
                    'Authorization': `Token ${this.userToken}`
                }
            })
                .then(response => {
                    console.log('Message sent:', response.data);
                    this.$emit('send');
                    this.closeModal();
                })
                .catch(error => {
                    console.error('There was an error!', error.response ? error.response.data : error);
                });
        },
        closeModal() {
            this.$emit('close');
        }
    }
};
</script>

<style scoped>
.modal-card {
    background-color: transparent;
    box-shadow: none;
}
.modal-close {
    color: white;
}
</style>
