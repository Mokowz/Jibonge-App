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

    mounted() {
        this.fetchBlogs()
    },

    methods: {
        async fetchBlogs() {
            // Fetch the blogs
            console.log(` Search: ${this.search}`)
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/blogs/?search=${this.search}`)
            this.blogs = response.data
            // console.log(`Search: ${search}`)
            console.log(`New Search: ${this.search}`)
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