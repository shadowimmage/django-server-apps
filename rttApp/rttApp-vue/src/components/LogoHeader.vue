<template>
    <div id='header' class='ph4 pt4 pb2'>
      <div id='header-top' class='cf'>
        <div id='logo' class='fl w-10 dib'>
          <router-link to='/'>
            <img src='../assets/logo.png' class='mw-100'>
          </router-link>
        </div>
        <div id='title' class='fl w-80'>
          <h1 class='f1 tl pl4'>Repair Task Tracker</h1>
        </div>
      </div>
      <div id='navigation' class='w-100 '>
        <router-link to='/'>
          <button class='dib f5 br-pill ba bw1 b--dark-gray bg-light-gray'>Create New</button>
        </router-link>
        <router-link to='/open'>
          <button class='dib f5 br-pill ba bw1 b--dark-gray bg-light-gray'>Open</button>
        </router-link>
        <router-link to='/search'>
          <button class='dib f5 br-pill ba bw1 b--dark-gray bg-light-gray'>Search</button>
        </router-link>
      </div>
    </div>
</template>

<<script>
export default {
  name: 'LogoHeader'
}
</script>

<style scoped>
h1 {
  margin-top: 0;
}
#logo img {
  max-height: 60px;
}
</style>

