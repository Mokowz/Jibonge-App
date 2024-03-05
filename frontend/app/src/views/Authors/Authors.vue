<template>
    <div class="flex container mx-auto p-10 md:py-10 md:px-0">

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

    },

    methods: {
        async fetchAuthors() {
            const response = await axios.get('http://127.0.0.1:8000/api/v1/authors/')

            if (response.status == 200) {
                this.authors = response.data
            }
        }
    }
}
</script>

<style>

</style>