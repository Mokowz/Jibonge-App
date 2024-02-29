<template>
    <!-- Flex Container -->
    <div class="flex flex-col text-white container mx-auto p-10">
      <!-- Heading -->
      <div class="flex flex-col space-y-3 border-b border-slate-500 pb-6">
        <h1 class="font-bold text-5xl">All Posts</h1>
        <input type="search" v-model="searchInput" class=" rounded-md px-4 py-2 max-w-sm bg-darkGrey/15" placeholder="Search blogs" @input="searchBlogs">
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
      // const response = await axios.get(`http://127.0.0.1:8000/api/v1/blogs/search/?search=${query}`)
      // this.search = query
      console.log(`Search Input ${this.searchInput}`)
      this.searchValue = this.searchInput
    }
  }
}
</script>
