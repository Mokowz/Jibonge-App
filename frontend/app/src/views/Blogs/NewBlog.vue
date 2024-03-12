<template>
  <div class="flex container mx-auto p-10 md:py-10 md:px-10">
    <form @submit.prevent="postNewBlog" class="flex flex-col space-y-10 w-full">
      <!-- Heading and Tags -->
      <div class="flex space-x-6 justify-between w-full">
        <div class="flex flex-col space-y-3 w-3/5">
          <label for="" class="font-semibold text-2xl">Add Title</label>
          <input v-model="title" type="text" class="bg-darkGrey/10 rounded-md px-8 py-3">
        </div>
        <div class="flex flex-col space-y-3">
          <label for="" class="font-semibold text-2xl">Add Tags</label>
          <select class="bg-darkGrey/10 rounded-md px-8 py-3" >
            <option value=""  v-for="tag in tags" key="tag.name">{{ tag.name }}</option>
          </select>
        </div>
        
      </div>

      <!-- Content -->
      <div class="flex flex-col space-y-4">
        <label for="" class="font-semibold text-2xl">Add Content</label>
        <textarea v-model="content" cols="30" rows="10" class="w-full rounded-md bg-darkGrey/10 px-8 py-3"></textarea>
      </div>

      <div>
        <input class="px-3 py-2 rounded-sm bg-yellow-500/75 hover:bg-yellow-500/90" type="submit" value="Create Post">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      tags: [],
      title: '',
      content: '',
      added_tags: []
    }
  },

  created() {
    this.fetchTags()
  },

  methods: {
    async postNewBlog() {
      const response = await axios.post('http://127.0.0.1:8000/api/v1/blogs/', {
        title: this.title,
        content: this.content,
        tags: this.added_tags,
      })

      if (response.status == 201) {
        this.$router.push('/blogs')
      }


    },

    async fetchTags() {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/tags/')

      if (response.status == 200) {
        this.tags = response.data
      }

    }
  },

}
</script>

<style>

</style>