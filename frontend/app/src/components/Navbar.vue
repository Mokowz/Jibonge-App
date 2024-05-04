<template>
  <nav class="text-white">
    <!-- Flex container -->
    <div class="flex container  justify-between mx-auto px-8 py-10 md:py-10 md:px-10">
        <!-- Logo -->
        <router-link to="/">
            <span class="text-3xl font-riot font-bold">Ji<span class="font-riot text-yellow-500">Bonge</span></span>
        </router-link>

        <!-- Hamburger Menu -->
        <span class="md:hidden absolute right-11 text-4xl duration-500 ease-in" @click="menuBtn()">
          <i class="duration-500 ease-in" :class="[open ? 'bi bi-x' : 'bi bi-list']"></i>
        </span>

        <!-- Menu -->
        <div class="md:flex items-center md:static absolute md:pb-10 pb-10 md:px-0 px-20 h-full md:h-auto  md:bg-inherit md:w-auto w-full top-20 duration-700 ease-in  md:space-x-8"
        :class="[open ? 'left-0' : 'left-[-100%]']" @click="menuBtn()">
            <router-link class="block md:flex my-6 md:my-0" to="/blogs">Blogs</router-link>
            <router-link class="block md:flex  my-6 md:my-0" to="/tags">Tags</router-link>
            <router-link class="block md:flex  my-6 md:my-0" to="/authors">Authors</router-link>

            <!-- Buttons -->
            <div class="md:flex block md:space-x-8" v-if="loggedInStatus()">
                <router-link class="block my-6" to="/">My Account</router-link>
                <router-link class="block my-6" to="/login" @click="logOut">Log Out</router-link>
            </div>

            <div class="md:flex block space-x-0 md:space-x-8" v-else>
                <router-link class="block my-6" to="/signup">Sign Up</router-link>
                <router-link class="block my-6" to="/login">Log In</router-link>
            </div>
          

        </div>
        
    </div>
    
  </nav>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      logInStatus: false,
      open: true,
    }
  },

  methods: {
    loggedInStatus() {
      return this.$store.state.loggedIn
    },

    menuBtn() {
      this.open = !this.open
    },

    async logOut() {
      const response = await axios.post('https://jibonge-app.onrender.com/api/v1/accounts/logout/')

      if (response.status === 200) {
        this.$store.commit('setLoggedIn', false)
        this.loggedInStatus()
      }
    },

    changeLogInStatus() {
      this.$store.commit('setLoggedIn', false)
    }

  }
}
</script>

<style>

</style>