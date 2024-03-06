<template>
  <div>
    <form action="" @submit.prevent="login" class="w-full mx-auto  flex flex-col space-y-4">
      <!-- Inputs -->
      <div class="flex flex-col items-center  space-y-3">
          <input type="email" placeholder="Email" v-model="email" required  class="p-2 w-full mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
          <input type="password" placeholder="Password" v-model="password" required class="p-2 w-full mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
      </div>
      
      <!-- Button -->
      <div class="flex flex-col space-y-2">
          <button type="submit" class="px-3 py-2 rounded-sm bg-yellow-500/75 hover:bg-yellow-500/90">Log In</button>
          <span>Don't have an account? <router-link to="/signup" class="text-yellow-400">Sign Up</router-link></span>
      </div>

      <!-- Sign Up with Google -->
      <a href="#" class="py-3 border border-gradient-to-r border-purple-500 border-pink-500 hover:border-pink-950">Log in with Google</a>
    </form>
  </div>
  
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      loggedIn: false,
    };
  },

  methods: {
    async login() {
      const response = await axios.post('http://127.0.0.1:8000/api/v1/accounts/login/', {
        email: this.email,
        password:this.password,
      })
      if (response.status === 200) {
        const token = response.data.key
        localStorage.setItem('token', token)
        
        this.changeLogin()
        this.loggedIn = true
        this.$router.push('/')
      }
    },

    changeLogin() {
      this.$store.commit('setLoggedIn', true)
    }
  }
}
</script>

<style>

</style>