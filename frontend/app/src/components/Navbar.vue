<template>
  <nav class="text-white">
    <!-- Flex container -->
    <div class="flex container justify-between mx-auto p-10">
        <!-- Logo -->
        <span class="text-2xl font-bold">Ji<span class="text-yellow-500">Bonge</span></span>
        <!-- Menu -->
        <div class="flex space-x-8">
            <router-link class="" to="/">Blogs</router-link>
            <router-link class="" to="/about">Tags</router-link>
            <router-link class="" to="/about">Profiles</router-link>

            <!-- Buttons -->
            <div class="flex space-x-8">
                <router-link to="/">Sign Up</router-link>
                <router-link to="/">Log In</router-link>
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