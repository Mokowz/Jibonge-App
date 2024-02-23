<template>
  <div class="container flex flex-col space-y-5 mx-auto p-10 md:px-0 md:py-10">
    <!-- Heading -->
    <div class="flex flex-col space-y-1 items-center border-b pb-6">
        <h4 class="font-bold  text-darkGrey">{{ blog.date_added }}</h4>
        <h3 class="text-4xl font-bold">{{ blog.title }}</h3>
    </div>
    <!-- Content section -->
    <div class="flex justify-between">
        <!-- Tags and Author Section -->
        <div class="flex flex-col">
            <!-- Author Section -->
            <div class="flex">
                <h4>By {{ blog.author }}</h4>
            </div>
        </div>
        <!-- Content -->
        <p class=" text-darkGrey">{{ blog.content }}</p>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { stringify } from 'postcss';

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
        }
    }
}
</script>

<style>

</style>