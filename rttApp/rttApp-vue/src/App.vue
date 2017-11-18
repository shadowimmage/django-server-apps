<template>
  <div id='app'>
    <Logo-header></Logo-header>
    <router-view></router-view>
  </div>
</template>

<script>
import LogoHeader from './components/LogoHeader'

export default {
  name: 'app',
  components: {
    LogoHeader
  }
}
</script>

<style>
#app {
  font-family: 'Segoe UI', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
body {
  background-color: #aaa;
}
</style>
