<template>
  <nav class="text-white">
    <!-- Flex container -->
    <div class="flex container justify-between mx-auto p-10 md:py-10 md:px-0">
        <!-- Logo -->
        <router-link to="/">
            <span class="text-3xl font-riot font-bold">Ji<span class="font-riot text-yellow-500">Bonge</span></span>
        </router-link>
        <!-- Menu -->
        <div class="hidden md:flex space-x-8">
            <router-link class="" to="/blogs">Blogs</router-link>
            <router-link class="" to="/tags">Tags</router-link>
            <router-link class="" to="/">Profiles</router-link>

            <!-- Buttons -->
            <div class="flex space-x-8" v-if="loggedInStatus()">
                <router-link to="/">My Account</router-link>
                <router-link to="/login" @click="logOut">Log Out</router-link>
            </div>

            <div class="flex space-x-8" v-else>
                <router-link to="/signup">Sign Up</router-link>
                <router-link to="/login">Log In</router-link>
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
    }
  },

  methods: {
    loggedInStatus() {
      return this.$store.state.loggedIn
    },

    async logOut() {
      const response = await axios.post('http://127.0.0.1:8000/api/v1/accounts/logout/')

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