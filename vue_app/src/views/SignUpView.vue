<template>
    <div class="page-sign-up">
      <div class="columns">
        <div class="column is-4 is-offset-4 box mt-6">
          <div id="main-content" class="mt-3">
            <h1 class="has-text-centered">Sign up</h1>
            <h1 class="mt-2 title has-text-centered">Create New Account</h1>
          </div>
  
          <form @submit.prevent="submitForm">
  
            <div class="field mt-6">
              <label>Username</label>
              <div class="control">
                <input type="text" class="input" v-model="username" placeholder="Username">
              </div>
            </div>
  
            <div class="field">
              <label>Email</label>
              <div class="control">
                <input type="email" class="input" v-model="email" placeholder="Email">
              </div>
            </div>
  
            <div class="company">
              <label>Company Name</label>
              <div class="control">
                <input type="text" class="input" v-model="companyName" placeholder="Company Name">
              </div>
            </div>
  
            <div class="field">
              <label>Address</label>
              <div class="control">
                <input type="text" class="input" v-model="address" placeholder="Address">
              </div>
            </div>
  
            <div class="field is-grouped">
              <div class="control is-expanded">
                <label>City</label>
                <div class="control">
                  <input type="tel" class="input" v-model="city" placeholder="City">
                </div>
              </div>
              <div class="control is-expanded">
                <label>State</label>
                <div class="control">
                  <input type="text" class="input" v-model="state" placeholder="State">
                </div>
              </div>
            </div>
  
            <div class="field is-grouped">
                <div class="is-expanded">
              <label>Zip Code</label>
              <div class="control">
                <input type="text" class="input" v-model="zipCode" placeholder="Zip Code">
              </div>
            </div>
            </div>
  
            <div class="field">
              <label>Password</label>
              <div class="control">
                <input type="password" class="input" v-model="password" placeholder="Password">
              </div>
            </div>
  
            <div class="field">
              <label>Repeat password</label>
              <div class="control">
                <input type="password" class="input" v-model="password2" placeholder="Repeat Password">
              </div>
            </div>
  
            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>
  
            <div class="field">
              <div class="control">
                <button class="button is-fullwidth is-success">Get Started</button>
              </div>
            </div>
  
            <hr>
            <div class="has-text-centered">
              Already have an account? <router-link to="/log-in">Sign in</router-link>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { toast } from 'bulma-toast'
  
  export default {
    name: 'SignUp',
    data() {
      return {
        username: '',
        email: '',
        address: '',
        city: '',
        state: '',
        zip_code: '',
        companyName: '',
        password: '',
        password2: '',
        errors: []
      }
    },
    mounted() {
      document.title = 'Sign Up | Predictive Roofing'
    },
    methods: {
      submitForm() {
        this.errors = []
  
        if (this.username === '') {
          this.errors.push('The username is missing')
        }
  
        if (this.password === '') {
          this.errors.push('The password is too short')
        }
  
        if (this.password !== this.password2) {
          this.errors.push('The passwords doesn\'t match')
        }
  
        if (!this.errors.length) {
          const formData = {
            username: this.username,
            email: this.email,
            address: this.address,
            city: this.city,
            state: this.state,
            zip_code: this.zipCode,
            companyName: this.companyName,
            password: this.password
          }
  
          axios
            .post("/api/v1/users/", formData)
            .then(response => {
              toast({
                message: 'Account created, please log in!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })
  
              this.$router.push('/log-in')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
  
                console.log(JSON.stringify(error.response.data))
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again')
                
                console.log(JSON.stringify(error))
              }
            })
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .page-sign-up {
    background-color: #ffffff;
  }
  
  .title {
    color: #363636;
  }
  
  .label {
    color: #363636;
  }
  
  .input {
    border-color: #363636;
  }
  
  .button.is-dark {
    background-color: #363636;
    color: #ffffff;
  }
  
  .notification.is-danger {
    background-color: #f5f5f5;
    color: #363636;
    border-left-color: #363636;
  }
  
  hr {
    border-color: #363636;
  }
  
  a.router-link {
    color: #363636;
    text-decoration: underline;
  }
  </style>
  