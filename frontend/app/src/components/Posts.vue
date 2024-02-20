<template>
  <div>
    <!-- Blog Cards -->
    <div v-for="blog in blogs" :key="blog.title" class="flex justify-between px-6 py-8 border-b border-slate-500">
        <span class="text-darkGrey">{{ blog.date_added }}</span>

        <!-- Info -->
        <div class="flex flex-col space-y-6">
            <!-- Heading -->
            <div class="flex flex-col">
                <div class="flex flex-col">
                    <h3 class="text-3xl font-bold">{{ blog.title }}</h3>

                    <!-- Tags -->
                    <!-- <div v-for="tag in blog.tags" :key="tag" class="inline">
                        <h4 class="text-yellow-300 font-semibold inline text-xl">{{ tag }}</h4>
                    </div> -->
                    <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-300 flex font-semibold  text-xl">{{ tag }}</h4>
                </div>
                
            </div>

            <!-- Content -->
            <p class="max-w-xl text-darkGrey">{{ blog.content }}</p>

            <!-- Read More btn -->
            <a href="#">Read More</a>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            blogs: [],
        }
    },

    mounted() {
        this.fetchBlogs()
    },

    methods: {
        async fetchBlogs() {
            // Fetch the blogs
            const response = await axios.get('http://127.0.0.1:8000/api/v1/blogs/')
            this.blogs = response.data
        }
    }
}
</script>

<style>

</style>