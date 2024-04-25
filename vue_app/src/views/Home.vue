<template>
    <div class="homepage-container">
      <div class="blur-background"></div> <!-- New element for the blurred background -->
      <div class="columns is-vcentered is-centered">
        <div class="column is-half has-text-centered">
          <p class="has-text-centered has-text-grey"> Preparing for the new future  </p>
          <h1 class="title is-1 has-text-white has-text-weight-medium is-family-secondary">
            Predictive Roofing
          </h1>
          <h1 class="title is-3 has-text-white has-text-weight-medium is-family-secondary">
            Helping customers be in their best in the moments that matter      
          </h1>
          <div class="buttons is-centered">
            <router-link to="/sign-up" class="button is-primary">Sign Up</router-link>
            <router-link to="/log-in" class="button is-light">Log In</router-link>
          </div>
        </div>
      </div>
    </div>
    <div style="height: 50px;"></div>
    <div class="columns is-centered ">
      <div class="column box mr-3 ml-6">
        <h2 class="title is-4 has-text-centered has-text-black">About Us</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </div>
      <div class="column box mr-3 ml-3">
        <h2 class="title is-4 has-text-centered has-text-black">Our Unique Hail Map Feature</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </div>
      <div class="column box mr-6 ml-3">
        <span class="icon">
          <font-awesome-icon :icon="['fad', 'tasks']" />
        </span>
        <h2 class="title is-4 has-text-centered has-text-black">Your Safety is Our #1 Priority</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style scoped>
  .homepage-container {
    position: relative;
    padding: 100px 0; /* Adjust padding as needed */
  }
  
  .blur-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('@/assets/home.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(7px); /* Apply the blur effect */
    z-index: -1; /* Ensure the blurred background is behind the content */
  }
  
  .buttons {
    margin-top: 20px;
  }
  
  .title,
  .subtitle {
    color: #fff; /* Adjust text color for better visibility */
  }
  </style>
  