<template>
    <div class="homepage-container">

        <h1 class="title is-4 company-name has-text-black">
            Predictive Roofing
        </h1>
        <img src="@/assets/PredictiveRoofing.png" alt="roofing" style="width: 30%; height: 30%;">



        <p class="subtitle is-4 has-text-black">
            Welcome to Predictive Roofing, your go-to solution for hail damage assistance. Leveraging cutting-edge AI technology, our app seamlessly connects customers with roofing expertise. From accurate damage prediction to swift response, Predictive Roofing ensures a seamless experience for homeowners in need. Experience the future of roofing solutions with Predictive Roofing – where innovation meets customer care.
        </p>


        <div class="button-container">
            <router-link to="/sign-up" class="button is-black signup-button">Sign Up</router-link>
            <router-link to="/log-in" class="button is-dark login-button">Log In</router-link>
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
    background-color: #ffffff;
    text-align: center;
    padding: 50px;
    color: #363636;
}

.company-name {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.subtitle {
    margin-bottom: 20px;
}

.button-container {
    margin-top: 20px;
}

.signup-button,
.login-button {
    margin-right: 10px;
    color: #ffffff;
}

.button.is-primary {
    background-color: #363636;
    border-color: transparent;
}

.button.is-info {
    background-color: #363636;
    border-color: transparent;
}

.button.is-primary:hover, .button.is-info:hover {
    opacity: 0.85;
}
</style>
