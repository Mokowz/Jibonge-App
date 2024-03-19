<template>
  <!-- Flex Container -->
  <div class="flex container  justify-center mx-auto  p-10">
    <!-- The Form Card Container -->
    <div class="flex flex-col space-y-6 items-center text-center rounded-lg border px-10 py-10 md:px-20 md:py-10  border-slate-200">
        <!-- Heading -->
        <div class="flex flex-col space-y-2">
            <h2 class="font-bold text-3xl text-yellow-500">Sign Up</h2>
            <p>Karibu Jibonge, bonga roho yako</p>
        </div>

        <!-- Actual Form -->
        <SignUpForm />
    </div>
  </div>
</template>

<script>
import SignUpForm from './SignUpForm.vue'

export default {
    components: { SignUpForm }
}
</script>

<style>

</style>