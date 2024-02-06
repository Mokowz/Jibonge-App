<template>
  <nav class="text-white">
    <!-- Flex container -->
    <div class="flex container justify-between mx-auto p-10">
        <!-- Logo -->
        <router-link to="/">
            <span class="text-3xl font-riot font-bold">Ji<span class="font-riot text-yellow-500">Bonge</span></span>
        </router-link>
        <!-- Menu -->
        <div class="flex space-x-8">
            <router-link class="" to="/blogs">Blogs</router-link>
            <router-link class="" to="/about">Tags</router-link>
            <router-link class="" to="/about">Profiles</router-link>

            <!-- Buttons -->
            <div class="flex space-x-8">
                <router-link to="/signup">Sign Up</router-link>
                <router-link to="/login">Log In</router-link>
            </div>
        </div>
        
    </div>
    
  </nav>
</template>

<script>
export default {

}
</script>

<style>

</style>