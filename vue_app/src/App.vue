<template>
  <header>
    <p><b>Dashboard</b></p>
    <div class="searchBar">
      <input type="text" placeholder="Search...">
      <button type="submit" >Search</button>
    </div>
  </header>
  <div class="sideNav">
    <div class="logo">
      <h1>Logo</h1>
    </div>
    <div class="overview">
      <p>Overview</p>
    </div>
    <div class="nav">
      <nav>
        <router-link to="/">Dashboard</router-link>
        <router-link to="/leads">Leads</router-link>
        <router-link to="/messages">Messages</router-link>
        <router-link to="/calendar">Calendar</router-link>
        <router-link to="/addLead">Add Lead</router-link>
      </nav>
    </div>
    <div class="bottomLinks">
      <router-link to="/settings">Settings</router-link>
      <router-link to="/login">Log Out</router-link>
    </div>   
  </div>

  <footer class="footer">
    <p>footer</p>
  </footer>
  
  <router-view/>
</template>

<script>
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.sideNav{
  height: 90vh;
  width: 200px;
  position: fixed;
  z-index:1;
  overflow-x: hidden;
  padding-top: 20px;
  background-color: white;
  display: flex;
  flex-direction: column;
  
}

.sideNav .logo,
.sideNav .overview,
.sideNav nav {
  padding: 10px;
}

.sideNav .logo h1,
.sideNav .overview p {
  margin: 0;
}

.overview {
  padding: 10px;
  align-self: flex-start; 
}

nav {
  color: black;
  display: flex;
  flex-direction: column;
}

.bottomLinks{
 display: flex;
 flex-direction: column;
 margin-top: auto;
}

header{
  height: 50px;
  background-color: white;
  position: fixed;
  width: 100%;
  z-index: 0;
  top: 0;
  margin-left: 200px;
  padding: 0px, 10px;
  display: flex;
}

footer{
    background-color: blue;
}
</style>
