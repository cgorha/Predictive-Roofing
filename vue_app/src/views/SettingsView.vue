<template>
    <div class="title">
        <h2> Settings </h2>
    </div>
    <div class="settings-container">

        <div class="settings-section">
            <h2>Notification Settings</h2>
            <label for="emailNotifications">Email Notifications:</label>
            <input type="checkbox" v-model="emailNotifications">
        </div>
        <div class="settings-section">
            <label for="alerts">Alerts: </label>
            <input type="checkbox" v-model="alerts">
        </div>
        <div class="settings-section">
            <h2>Theme Settings</h2>
            <label for="darkMode">Dark Mode:</label>
            <input type="checkbox" v-model="darkMode">
        </div>
        <div class="settings-section">
            <h2>Language Settings</h2>
            <label for="language">Language:</label>
            <select v-model="language">
                <option value="en">English</option>
                <option value="fr">French</option>
                <option value="es">Spanish</option>

            </select>

        </div>
        <br>
        <br>
        <button @click="saveSettings" class="save-button">Save Settings</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            alerts: '',
            emailNotifications: false,
            darkMode: false,
            language: 'en'
        };
    },
    methods: {
        saveSettings() {
            // Perform saving logic here
            alert("Settings have been saved!");
        }
    }
};
</script>


<style scoped>
.settings-container {
    width: 300px;
    height: 300px;
    margin: auto;
    padding: 20px;
    background-color: lightgray;
    border: 5px solid blue;
    border-radius: 20px;


}

.settings-section {
    margin-bottom: 20px;
}

.title {
    text-size-adjust: 50%;
    text-align: center;
}

.save-button {
    background-color: grey;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    text-align: center;
}

</style>