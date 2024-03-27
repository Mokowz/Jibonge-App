<template>
  <div>
    <!-- Blog Cards -->
    <div v-for="blog in blogs" :key="blog.title" class="flex flex-col-reverse justify-between  py-8 border-b border-slate-500 md:flex-row md:px-6">
        <span class="text-darkGrey w-1/4">{{ formatDate(blog.date_added) }}</span>

        <!-- Info -->
        <div class="flex flex-col w-full md:w-3/4 space-y-6 mb-4 md:mb-0">
            <!-- Heading -->
            <div class="flex flex-col">
                <div class="flex flex-col">
                    <h3 class="text-3xl font-bold">{{ blog.title }}</h3>
                    <div class="flex flex-row space-x-2">
                        <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-300  font-semibold  text-lg">{{ tag.name.toUpperCase() }}</h4>
                    </div>
                </div>
                
            </div>

            <!-- Content -->
            <p class="max-w-xl text-darkGrey">{{ blog.content.slice(0,200) }}...</p>

            <!-- Read More btn -->
            <router-link :to="{name: 'blog', params: {id: blog.id}}" class="text-yellow-300 ">
                Read More &#62;
            </router-link>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    props:['search'],
    data() {
        return {
            blogs: [],
        }
    },

    created() {
        this.fetchBlogs()
    },

    watch: {
        search(newValue, oldValue) {
            this.fetchBlogs()
        }
    },

    methods: {
        async fetchBlogs() {
            // Fetch the blogs
            const response = await axios.get(`https://jibonge-app.onrender.com/api/v1/blogs/?search=${this.search}`)
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