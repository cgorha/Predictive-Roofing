<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css">
    <div class="container">
        <form @submit.prevent="addLead" class="box">
                <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input v-model="newLead.name" placeholder="Name" required>
                        </div>
                    </div>
                    <div class="phoneNumber">
                          <label>Phone Number</label>
                          <div class="control">
                              <input v-model="newLead.phone" placeholder="Phone" required>
                          </div>
                    </div>

                    <div class="field">
                        <label>Date</label>
                        <div class="control">
                            <input v-model="newLead.date" type="date" placeholder="Date" required>
                        </div>
                    </div>

                    <div class="field">
                        <label>Zip Code</label>
                        <div class="control">
                            <input v-model="newLead.zip_code" placeholder="Zip Code" required>
                        </div>
                    </div>

                    <div class="field">
                        <label>Insurance Company</label>
                        <div class="control">
                            <input v-model="newLead.insurance_company" placeholder="Insurance Company" required>
                        </div>
                    </div>

                    <div class="field">
                        <select v-model="newLead.status" required>
                            <option value="Pending">Pending</option>
                            <option value="In Progress">In Progress</option>
                            <option value="Completed">Completed</option>
                         </select>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-primary">Add Lead</button>
                        </div>
                    </div>

                    <hr>
            </form>
    </div>
</template>
<script>
import axios from 'axios';
import {mapActions, mapState} from "vuex";

export default {
    data() {
        return {
            tableColumns: ['Name', 'Phone', 'Date', 'Zip Code', 'Insurance Company', 'Status'],
            tableItems: [],
            newLead: {
                name: '',
                phone: '',
                date: '',
                zip_code: '',
                insurance_company: '',
                status: 'Pending',
            },
        };
    },
    computed: {
        ...mapState(['userToken']),
    },
    methods: {
        async addLead() {
            try {
                const response = await axios.post('/leads/', this.newLead, {
                    headers: { "Authorization": `Token ${this.userToken}` }
                });
                this.tableItems.push(response.data);
                this.newLead = { name: '', phone: '', date: '', zip_code: '', insurance_company: '', status: 'Pending' }; // Reset form
            } catch (error) {
                console.error('There was an error adding the lead:', error.response ? error.response.data : error);
            }
        },
    },
};
</script>
<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 50px;

    }

    .button {
        cursor: pointer;
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    .button:hover {
        background-color: #0056b3;
    }
</style>