<template>
    <!-- Flex Container -->
    <div class="flex flex-col text-white container mx-auto p-10">
      <!-- Heading -->
      <div class="flex flex-col space-y-3 border-b border-slate-500 pb-6">
        <h1 class="text-4xl font-bold">Karibu Jibonge, a one-stop <span class="text-yellow-500">magazine</span> for all you Swahili and sheng lovers</h1>
        <p class="text-darkGrey">Jibonge offers a vibrant space where Swahili and Sheng aficionados can delve into
           a diverse array of content. From language insights to cultural explorations, it's your go-to platform for immersive experiences 
           and community connections in the realm of East African languages.
        </p>
      </div>

      <!-- Posts -->
      <Posts />


    </div>
</template>

<script>
import Posts from '@/components/Posts.vue';

export default {
  name: 'HomeView',
  components: { Posts  }
}
</script>
