<template>
<div class="container">
  <div class="map">
    <!-- Your map content goes here -->
    <!-- You can embed a map component or any other content for the map -->
    Map Content
  </div>

  <div class="legend">
    <!-- Your legend content goes here -->
    <!-- You can add legends, key information, or any other content related to the map -->
    Legend Content
  </div>
</div>
</template>

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
