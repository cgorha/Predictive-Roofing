<template>
    <div class="page-log-in">
        <div class="columns is-centered">
            <div class="column is-7 box mt-6">
                <div class="columns is-vcentered">
                    <div class="column">
                        <img src="../../public/log_in.png" class="image-left" alt="Sign Up Image">
                    </div>
                    
                    <div class="column">
                        
                        <h1 class="title has-text-centered">Log In</h1>
                        <p class="subtitle has-text-centered"> Welcome back to Predictive Roofing</p>
                        
                        
                        <form @submit.prevent="submitForm">
                            <div class="field">
                                <div class="control has-icons-left">
                                    <input type="text" class="input" v-model="username" placeholder="Username">
                                    <span class="icon is-small is-left">
                                        <font-awesome-icon icon="user" />
                                    </span>
                                </div>
                            </div>
                            
                            <div class="field">
                                <div class="control has-icons-left">
                                    <input type="password" class="input" v-model="password" placeholder="Password">
                                    <span class="icon is-small is-left">
                                        <font-awesome-icon icon="key" />
                                    </span>
                                </div>
                            </div>
                            
                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                            
                            <div class="field">
                                <div class="control">
                                    <button class="button is-fullwidth is-success">Log in</button>
                                </div>
                            </div>
                            
                            <hr>
                            <div class="has-text-centered">
                                Don't have an account? <router-link to="/sign-up">Click here</router-link> to sign up!
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        };
    },
    mounted() {
        document.title = 'Log In | Predictive Roofing';
    },
    methods: {
        ...mapActions(['login']),
        submitForm() {
            const credentials = {
                username: this.username,
                password: this.password
            };

            this.login(credentials)
                .catch(error => {
                    this.errors.push('Login failed. Please check your credentials.');
                    console.error('Login error:', error);
                });
        }
    }
};
</script>