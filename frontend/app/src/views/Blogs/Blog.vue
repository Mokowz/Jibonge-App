<template>
  <div class="container flex flex-col space-y-5 mx-auto p-10 md:px-0 md:py-10">
    <!-- Heading -->
    <div class="flex flex-col space-y-1 items-center border-b pb-6">
        <h4 class="font-bold  text-darkGrey">{{ blog.date_added }}</h4>
        <h3 class="text-4xl font-bold">{{ blog.title }}</h3>
    </div>
    <!-- Content section -->
    <div class="flex justify-between space-x-5">
        <!-- Tags and Author Section -->
        <div class="flex flex-col w-1/5">
            <!-- Author Section -->
            <div class="flex flex-col pb-6 border-b">
                <!-- <h4>By {{ fullName(blog.author) }}</h4> -->
                <h2>AUTHOR</h2>
                <h4>By Ronny Kerosi</h4>
            </div>
            <div class="flex flex-col py-6 border-b">
                <h2>TAGS</h2>
                <span v-for="tag in blog.tags" key="tag.name">{{ tag.name }}</span>
            </div>
            <div class="flex flex-col py-6 border-b">
                <button @click="goBack">Back to Blogs</button>
            </div>

        </div>
        <!-- Content -->
        <div class="w-4/5">
            <p class=" text-darkGrey">{{ blog.content }}</p>
        </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    props: {
        id: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            blog: []
        }
    },
    created() {
        this.fetchSingleBlog()
    },
    methods: {
        async fetchSingleBlog() {
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/blogs/${this.$route.params.id}/`)
            this.blog = response.data
            console.log(this.blog)
        },
        fullName(value) {
            const author = `${value.user['first_name']} ${value.user['last_name']}`
            console.log(`User ${author}`)
            return author
        },
        goBack() {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
        }
    }
}
</script>

<style>

</style>