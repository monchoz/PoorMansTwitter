<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  color: #777;
  background: #4CAF50;
}

img {
  position: absolute;
  left: 0;
  top: 0;
}
</style>
