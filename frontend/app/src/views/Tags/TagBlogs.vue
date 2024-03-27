<template>
    <!-- Flex Container -->
    <div class="flex flex-col text-white container mx-auto px-8 md:py-10 md:px-10">
        <!-- Heading and Add Button -->
        <div class="flex justify-between items-center w-full border-b border-slate-500 pb-6">
            <!-- Heading -->
            <div class="flex flex-col space-y-3">
                <h1 class="font-bold text-4xl md:text-5xl">{{ name }} Posts</h1>
                <!-- <input type="search" v-model="searchInput" class=" rounded-md px-4 py-2 max-w-sm bg-darkGrey/15" placeholder="Search blogs" @input="searchBlogs"> -->
            </div>
        </div>

        <div v-for="blog in blogs" :key="blog.title" class="flex flex-col-reverse justify-between md:px-6 py-8 border-b border-slate-500 md:flex-row">
            <span class="text-darkGrey">{{ formatDate(blog.date_added) }}</span>

            <!-- Info -->
            <div class="flex flex-col space-y-6 mb-4 md:mb-0">
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
import axios from 'axios'

export default {
    props: {
        id: {
            required: true,
            type: String,
        },
        name: {
            required: true,
            type: String,
        },
    },

    data() {
        return {
            blogs: [],
            name: ''
        }
    },

    created() {
        this.fetchTagBlog()
    },

    methods: { 
        async fetchTagBlog() {
            const response = await axios.get(`https://jibonge-app.onrender.com/api/v1/blogs/filter/?tags=${this.$route.params.id}`)

            if (response.status == 200) {
                this.blogs = response.data
                // console.log(`Name: ${this.name}`)
                console.log(this.blogs)
            }
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
    }

}
</script>

<style>

</style>