<template>
    <!-- Flex Container -->
    <div class="flex flex-col text-white container mx-auto p-10">
      <!-- Heading -->
      <div class="flex flex-col space-y-3 border-b border-slate-500 pb-6">
        <h1 class="font-bold text-5xl">All Posts</h1>
        <input type="search" class=" rounded-md px-4 py-2 max-w-sm bg-darkGrey/15" placeholder="Search blogs">
      </div>

      <!-- Posts -->
      <Posts />


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
      blogs: []
    }
  },

  methods: {
    aync searchBlogs(query) {
      const response = await axios.get('')
      this.blogs = response.data
    }
  }
}
</script>
