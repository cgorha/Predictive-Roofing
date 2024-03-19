<template>
    <div class="table-container">

        <table>
            <thead>
            <tr>
                <th v-for="column in tableColumns" :key="column">{{ column }}</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in tableItems" :key="item.id">
                <td>{{ item.name }}</td>
                <td>{{ item.phone }}</td>
                <td>{{ item.date }}</td>
                <td>{{ item.zip_code }}</td>
                <td>{{ item.insurance_company }}</td>
                <td>{{ item.status }}</td>
            </tr>
            </tbody>
        </table>
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
    created() {
        this.fetchLeads();
    },
    computed: {
        ...mapState(['userToken']),
    },
    methods: {
        async fetchLeads() {
            try {
                const response = await axios.get('/leads/', {
                    headers: { "Authorization": `Token ${this.userToken}` }
                });
                this.tableItems = response.data;
            } catch (error) {
                console.error('There was an error fetching the leads:', error);
            }
        },
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
.table-container {
    max-width: 800px;
    margin: 0 auto;
    overflow-x: auto;
}

form {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 20px;
    background: #f4f4f4;
    padding: 20px;
    border-radius: 8px;
}

input, select {
    flex: 1 1 180px; /* Grow to fill space, but not smaller than 180px */
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

button {
    cursor: pointer;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #0056b3;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    text-align: left;
    padding: 8px;
    border: 1px solid #ccc;
}

th {
    background-color: #007bff;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>

