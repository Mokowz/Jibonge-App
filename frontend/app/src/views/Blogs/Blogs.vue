<template>
    <!-- Flex Container -->
    <div class="flex flex-col text-white container mx-auto px-8 md:py-10 md:px-8">
      <!-- Heading and Add Button -->
      <div class="flex justify-between items-center w-full border-b border-slate-500 pb-6">
        <!-- Heading -->
        <div class="flex flex-col space-y-3">
          <h1 class="font-bold text-4xl md:text-5xl">All Posts</h1>
          <input type="search" v-model="searchInput" class=" rounded-md px-4 py-2 max-w-sm bg-darkGrey/15" placeholder="Search blogs" @input="searchBlogs">
        </div>

        <!-- Add Blog -->
        <div v-if="loggedIn()">
          <router-link to="/new/blog" class="rounded-md px-4 py-2 bg-yellow-500/75 font-medium ">Add New Blog</router-link>
        </div>


      </div>
      

      <!-- Posts -->
      <Posts :search="searchValue" />


    </div>
</template>

<script>
import Posts from '@/components/Posts.vue';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: { Posts  },

  data() {
    return {
      searchInput: '',
      searchValue: '',
      searchResults: [],
    }
  },

  methods: {
      searchBlogs() {
      this.searchValue = this.searchInput
    },

    loggedIn() {
      return this.$store.state.loggedIn
    }
  }
}
</script>
