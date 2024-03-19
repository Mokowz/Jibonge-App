<template>
  <!-- Flex Container -->
  <div class="flex container  justify-center mx-auto  px-8 md:py-10 md:px-10">
    <!-- The Form Card Container -->
    <div class="flex flex-col space-y-6 items-center text-center rounded-lg border px-10 py-10 md:px-20 md:py-10 border-slate-200">
        <!-- Heading -->
        <div class="flex flex-col space-y-2">
            <h2 class="font-bold text-3xl text-yellow-500">Log In</h2>
            <p>Umerudi kubonga sio?</p>
        </div>

        <!-- Actual Form -->
        <LoginForm />
    </div>
  </div>
</template>

<script>
import LoginForm from './LoginForm.vue'


export default {
    components: { LoginForm }
}
</script>

<style>

</style>