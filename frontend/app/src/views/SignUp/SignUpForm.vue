<template>
  <form action="" class="w-full items-center flex flex-col space-y-4">
    <!-- Inputs -->
    <div class="flex flex-col items-center  space-y-2">
        <input type="text" placeholder="First Name" class="p-1 bg-transparent text-slate-50 border rounded-sm border-slate-50">
        <input type="text" placeholder="Last Name" class="p-1 bg-transparent text-slate-50 border rounded-sm border-slate-50">
        <input type="email" placeholder="Email" class="p-1 bg-transparent text-slate-50 border rounded-sm border-slate-50">
        <input type="password" placeholder="Password" class="p-1 bg-transparent text-slate-50 border rounded-sm border-slate-50">
        <input type="password" placeholder="Confirm Password" class="p-1 bg-transparent text-slate-50 border rounded-sm border-slate-50">
    </div>
    
    <!-- Button -->
    <div class="flex flex-col space-y-1">
        <button type="submit" class="px-3 py-2 rounded-sm bg-yellow-500">Sign Up</button>
        <span>Already have an account? <router-link to="/" class="text-yellow-400">Log In</router-link></span>
    </div>
  </form>
</template>

<script>
export default {

}
</script>

<style>

</style>