<template>
  <div>
    <form action="" class="w-full mx-auto  flex flex-col space-y-4">
      <!-- Inputs -->
      <div class="flex flex-col items-center   space-y-3">
          <input type="email" placeholder="Email" class="p-1 w-full mx-auto bg-transparent text-slate-50 border rounded-sm border-slate-50">
          <input type="password" placeholder="Password" class="p-1 w-full mx-auto bg-transparent text-slate-50 border rounded-sm border-slate-50">
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
export default {

}
</script>

<style>

</style>