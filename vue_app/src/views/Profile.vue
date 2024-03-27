<template>
    <h1 class="title has-text-centered">Profile Information</h1>
    <section class="section">
        


        <div class="container">
            <!-- User Information Box -->
            <div class="box">
                <div class="user-info-box">
                    <h2 class="title has-text-centered">User Information</h2>
                    <div class="container">
                        <p><strong>Company Name:</strong> {{ profile.companyName }}</p>
                        <p><strong>Name:</strong> {{ profile.name }}</p>
                        <p><strong>Email:</strong> {{ profile.email }}</p>
                        <p><strong>Phone Number:</strong> {{ profile.phoneNumber }}</p>
                    </div>
                </div>
            </div>

            <div class="box">
                <h2 class="title has-text-centered">Update Profile Information</h2>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Company Name</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Company Name" v-model="profile.companyName" required>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Your Name" v-model="profile.name" required>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Email</label>
                        <div class="control">
                            <input class="input" type="email" placeholder="name@example.com" v-model="profile.email" required>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Phone Number</label>
                        <div class="control">
                            <input class="input" type="tel" placeholder="+1234567890" v-model="profile.phoneNumber" required>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Company Profile Picture</label>
                        <div class="file has-name">
                            <label class="file-label">
                                <input class="file-input" type="file" name="profile_picture" @change="previewImage">
                                <span class="file-cta">
                  <span class="file-icon">
                    <i class="fas fa-upload"></i>
                  </span>
                  <span class="file-label">Choose a file…</span>
                </span>
                                <span class="file-name" v-if="profile.imageName">{{ profile.imageName }}</span>
                            </label>
                        </div>
                    </div>

                    <div class="field is-grouped">
                        <div class="control">
                            <button class="button is-black">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>

<script>


export default {
    data() {
        return {
            profile: {
                companyName: '',
                name: '',
                email: '',
                phoneNumber: '',
                imageName: '',
                imageFile: null,
            },
            
        };
    },
    methods: {
        submitForm() {
            // Implement form submission logic here
            console.log(this.profile);
            // For example, use Axios to send a request to your server
        },
        previewImage(event) {
            this.profile.imageName = event.target.files[0].name;
            this.profile.imageFile = event.target.files[0];
            // Optionally implement image preview functionality
        },
    },
};
</script>

<style scoped>
.section {
    background-color: #ffffff;
}
.title, .label {
    color: #363636;
}
.file-label {
    border-color: #363636;
}
.button.is-black {
    background-color: #363636;
    color: #ffffff;
}
.box {
    max-width: 800px;
    margin: auto;
    padding: 20px;
}
</style>
