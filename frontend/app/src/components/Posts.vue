<template>
  <div>
    <!-- Blog Cards -->
    <div v-for="blog in blogs" :key="blog.title" class="flex justify-between px-6 py-8 border-b border-slate-500">
        <span class="text-darkGrey">{{ formatDate(blog.date_added) }}</span>

        <!-- Info -->
        <div class="flex flex-col space-y-6">
            <!-- Heading -->
            <div class="flex flex-col">
                <div class="flex flex-col">
                    <h3 class="text-3xl font-bold">{{ blog.title }}</h3>
                    <div class="inline-block">
                        <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-300 flex font-semibold  text-lg">{{ tag.name.toUpperCase() }}</h4>
                    </div>
                </div>
                
            </div>

            <!-- Content -->
            <p class="max-w-xl text-darkGrey">{{ blog.content.slice(0,200) }}...</p>

            <!-- Read More btn -->
            <a href="#" class="text-yellow-200 underline">Read More</a>
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
        },

        formatDate(value) {
            if (!value) return '';
            const options = {
                month: 'long',
                day: 'numeric',
                year: 'numeric',
            };
            return new Date(value).toLocaleDateString(options);
            // return new Intl.DateTimeFormat('en-US', options).format(value)
        },
    },

    filters: {
        
    }
}
</script>

<style>

</style>