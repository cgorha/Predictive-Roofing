<!--
      <h1 class="title is-1">Predictive Roofing</h1>
      <p class="subtitle is-4">Your trusted partner in roofing solutions.</p>
-->
<template>
  <div class="homepage-container">
    <!-- Company Name -->
    <h1 class="title is-4 company-name">
      Predictive Roofing
    </h1>

    <!-- General Company Information -->
    <p class="subtitile is-4">
      Welcome to Predictive Roofing, your go-to solution for hail damage assistance. Leveraging cutting-edge AI technology, our app seamlessly connects customers with roofing expertise. From accurate damage prediction to swift response, Predictive Roofing ensures a seamless experience for homeowners in need. Experience the future of roofing solutions with Predictive Roofing – where innovation meets customer care.
    </p>

    <!-- Buttons for Sign Up and Log In -->
    <div class="button-container">
      <router-link to="/sign-up" class="button is-primary signup-button">Sign Up</router-link>
      <router-link to="/log-in" class="button is-info login-button">Log In</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
.homepage-container {
  text-align: center;
  padding: 50px;
}

.company-name {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.button-container {
  margin-top: 20px;
}

.signup-button,
.login-button {
  margin-right: 10px;
}
</style>
