<template>
    <div class="table-container">
        
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th v-for="column in tableColumns" :key="column">{{ column }}</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item,index) in tableItems" :key="item.id">
                    <td>{{ index + 1 }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ formatPhoneNumber(item.phone) }}</td>
                    <td>{{ item.date }}</td>
                    <td>{{ item.zip_code }}</td>
                    <td>{{ item.insurance_company }}</td>
                    <td :class="statusColors[item.status]"> {{ item.status }} </td>
                    <td><font-awesome-icon :icon="statusIcons[item.status]" /></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
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

            statusIcons: {
                'Pending' : 'clock',
                'In Progress': 'spinner',
                'Completed': 'check',
            },

            statusColors: {
                'Pending': 'status-pending',   
                'In Progress': 'status-in-progress', 
                'Completed': 'status-completed', 
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

        formatPhoneNumber(phoneNumber) {
            if (!phoneNumber) return ''; // Handle empty values

            // Only consider numerical digits
            const cleaned = ('' + phoneNumber).replace(/\D/g, '');
            const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);  

            if (match) {
            return '(' + match[1] + ') ' + match[2] + '-' + match[3];
            }

            return phoneNumber; // Return original value if formatting fails
        },

    },
};
</script>

<style>
.table-container {
    max-width: 1200px;
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
    border: 1px solid #fdf6f6;
    border-radius: 4px;
    font-size: 16px;
}

button {
    cursor: pointer;
    padding: 10px 20px;
    background-color: #35fce5;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #4dffde;
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
    font-size: 18px; 
    font-weight: bold;
    padding: 15px;
}

th {
    background-color: #31d0b6;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

.status-pending {
  background-color: #ffe0b2; 
}

.status-in-progress {
  background-color: #b3e5fc; 
}

.status-completed {
  background-color: #d4edda; 
}

</style>

