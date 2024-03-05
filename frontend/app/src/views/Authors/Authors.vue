<template>
    <div class="flex space-x-8 container mx-auto p-10 md:py-10 md:px-0">
        <div v-for="author in authors" key="author.id" class="w-1/2 flex justify-around py-8 px-14 bg-darkGrey/10 items-center rounded-lg">

            <h3 v-if="author.user.first_name" class="bg-transparent font-semibold text-xl">{{ author.user.first_name }} {{ author.user.last_name }}</h3>
            <h3 v-else class="bg-transparent font-semibold text-xl">Author X</h3>
            <div class="w-32 h-32 bg-transparent">
                <img :src="author.profile_pic" class="w-full h-full rounded-full">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            authors: [],
        }
    },

    created() {
        this.fetchAuthors()
    }, 

    methods: {
        async fetchAuthors() {
            const response = await axios.get('http://127.0.0.1:8000/api/v1/authors/')

            if (response.status == 200) {
                this.authors = response.data
                console.log(this.authors)
            }
        }
    }
}
</script>

<style>

</style>