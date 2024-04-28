<template>
  <div class="homepage-container">
    <div class="blur-background"></div> <!-- New element for the blurred background -->
    <div class="columns is-centered">
      <div class="column is-four-fifths">
        <h1 class="title is-1 has-text-white has-text-weight-medium is-family-secondary">
          Prepare for the future with us,
        </h1>
        <h1 class="subtitle has-text-white has-text-weight-medium is-family-secondary">
          Helping customers be in their best in the moments that matter      
        </h1>
        <div class="buttons is-centered mt-10">
          <router-link to="/sign-up" class="button is-primary">Get Started</router-link>
          <router-link to="/log-in" class="button is-light">Log In</router-link>
        </div>
        
        <div class="buttons is-centered">
          <button class="button is-light scroll-down-button">
              <font-awesome-icon icon="chevron-down" style="color: aliceblue;"/> 
          </button>
      </div>
        
      </div>
    </div>
  </div>
  <div style="height: 340px;">
  </div>
  <div class="about-us-section">
    <h2 class="title has-text-centered has-text-black	">About Us</h2>
    <p class="has-text-centered">
      We believe preparedness is key when it comes to unpredictable weather events.  Our service combines advanced hail prediction technology with user-friendly tools to help you make informed decisions about safeguarding your property.</p>
    </div>
    <div style="height: 80px;"></div>
      <div class="columns is-multiline"> <div class="column is-one-third">
        <h1 class="title has-text-centered has-text-black">Hail Map</h1>
        <figure class="image">
          <img src="../../public/map_feature.png" alt="Image Description 1">
        </figure>
        <p class="has-text-centered info-p">Our interactive hail map offers location-specific insights. Visualize hail patterns and make informed decisions to safeguard your property.</p>
      </div>
      <div class="column is-one-third">
        <h1 class="title has-text-centered has-text-black">Stay Connected</h1>
        <figure class="image">
          <img src="../../public/Message_feature.png" alt="Image Description 2">
        </figure>
        <p class="has-text-centered info-p">Keep in touch with other users and customers with our messaging system.</p>
      </div>
      <div class="column is-one-third">
        <h1 class="title has-text-centered has-text-black">Keep track of Leads</h1>
        <figure class="image">
          <img src="../../public/Leads_feature.png" alt="Image Description 3">
        </figure>
        <p class="has-text-centered info-p">Manage your leads seamlessly. Track status, follow-ups, and analyze your outreach with our user-friendly lead management tools.</p>
      </div>
    </div>
    <div style="height: 120px;"></div>
  
</template>
  
  <script>
  export default {
    name: 'Home',

      methods: {
      scrollDown() {
        const aboutUsSection = document.querySelector('.about-us-section');
        aboutUsSection.scrollIntoView({ behavior: 'smooth' });
      },
    },
    mounted() { /* Execute the function when the component is mounted */
      const scrollButton = document.querySelector('.scroll-down-button');
      scrollButton.addEventListener('click', this.scrollDown);
    }
  };

  
  </script>
  
  <style scoped>
  .homepage-container {
  position: relative;
  padding: 100px 0; /* Adjust padding as needed */
  text-align: center; /* Center align the content */
}
  
  .blur-background {
    position: absolute;
    top: 0;
    width: 100%;
    height: 150%;
    background-image: url('@/assets/home.jpg');
    
    background-repeat: no-repeat;
    filter: blur(7px); /* Apply the blur effect */
    z-index: -1; /* Ensure the blurred background is behind the content */
    background-size: 120%; /* Zoom in */
    background-position: 50% 30%; /* Adjust positioning */ 
  }
  
  .buttons {
    margin-top: 80px;
    text-align: center;
  }
  
  .title,
  .subtitle {
    color: #fff; /* Adjust text color for better visibility */
  }

  .about-us-section {
    width: 60%; /* Adjust the percentage as desired */
    margin: 0 auto;  /* Center the content */
    padding: 30px;
  }

  .image{
    width: 65%; /* Adjust the percentage as desired */
    margin: 0 auto;  /* Center the content */
  }

  .info-p{
    padding: 20px;
  }

  .scroll-down-button {
   background-color: transparent;
  }



  </style>
  