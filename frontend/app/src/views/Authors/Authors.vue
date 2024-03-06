<template>
    <div class="flex flex-col space-y-8 md:space-x-8 container mx-auto px-8 md:flex-row md:py-10 md:px-10 md:space-y-0">
        <div v-for="author in authors" key="author.id" class="w-full flex justify-around py-6 px-0 bg-darkGrey/10 items-center rounded-lg md:w-1/2 md:py-8 md:px-14">

            <h3 v-if="author.user.first_name" class="bg-transparent font-semibold text-xl">{{ author.user.first_name }} {{ author.user.last_name }}</h3>
            <h3 v-else class="bg-transparent font-semibold text-xl">Author X</h3>
            <div class="w-20 h-20 bg-transparent md:w-32 md:h-32">
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