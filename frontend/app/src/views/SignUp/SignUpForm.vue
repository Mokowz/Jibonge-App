<template>
  <form action="" @submit.prevent="signUp" class="w-full mx-auto  flex flex-col space-y-4">
    <!-- Inputs -->
    <div class="flex w-full flex-col items-center p-0 m- m-0  space-y-4">
        <input type="text" placeholder="First Name" v-model="first_name" class="p-3 w-full  mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
        <input type="text" placeholder="Last Name" v-model="last_name" class="p-3 w-full  mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
        <input type="email" placeholder="Email" v-model="email" class="p-3 w-full  mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
        <input type="password" placeholder="Password" v-model="password1" class="p-3 w-full  mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
        <input type="password" placeholder="Confirm Password" v-model="password2" class="p-3 w-full  mx-auto  text-slate-50  rounded-md bg-darkGrey/15 ">
    </div>
    
    <!-- Button -->
    <div class="flex flex-col space-y-2">
        <button type="submit" class="px-3 py-2 rounded-sm bg-yellow-500/75 hover:bg-yellow-500/90">Sign Up</button>
        <span>Already have an account? <router-link to="/login" class="text-yellow-400">Log In</router-link></span>
    </div>

    <!-- Sign Up with Google -->
    <!-- <a href="#" class="py-3 border border-gradient-to-r border-purple-500 border-pink-500 hover:border-pink-950">Sign up with Google</a> -->
  </form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password1: '',
      password2: '',
    }
  },

  methods: {
    async signUp() {
      const response = await axios.post('https://jibonge-app.onrender.com/api/v1/accounts/registration/', {
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name,
          password: this.password1,
          // password2: this.password2,
      })

      if (response.status === 201) {
        this.$router.push('/login')
      }
    },

    checkModels() {
      console.log(`Email: ${this.email}`)
      console.log(`First Name: ${this.first_name}`)
      console.log(`Last Name: ${this.last_name}`)
      console.log(`Password1: ${this.password1}`)
      console.log(`Password2: ${this.password2}`)
    }
  }
}
</script>

<style>

.input-field {
  padding: 0.75rem; /* Adjust as needed */
  margin: 0.5rem 0; /* Adjust as needed */
}

</style>