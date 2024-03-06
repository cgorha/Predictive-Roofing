<template>
<div class="container">
  <div class="map">
    Map Content
      <GoogleMaps :mapOptions="{ zoom: 10, center: { lat: -33.8688, lng: 151.2093 } }"/>
  </div>

  <div class="legend">
    Legend Content
  </div>
</div>
</template>

<script>
import GoogleMaps from '../components/googleMaps.vue';

export default {
    name: 'App',
    components: {
        GoogleMaps
    }
};
</script>

<style>
  .container {
    display: flex;
    flex-direction: row;
    
  }

  .map {
    flex: 1;
    height: 400px;
    font-size: 20px;
    margin-top: 40px; 
  }

  .legend {
    width: 200px;
    font-size: 20px; 
    margin-top: 40px; 
  }
</style>
