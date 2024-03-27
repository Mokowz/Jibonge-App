<template>
  <div class="container mx-auto px-8 md:py-10 md:px-10">
    <div class="flex">
        <div v-for="tag in tags" key="tag.id"  class="py-3 px-8 m-4 border rounded-sm">
            <router-link   :to="{name: 'tagsList', params: {id: tag.id}}">
                {{ tag.name }}            
            </router-link>
        </div> 
        
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            tags: []
        }
    },
    created() {
        this.fetchTags()
    },
    methods: {
        async fetchTags() {
            const response = await axios.get('https://jibonge-app.onrender.com/api/v1/tags/')
            this.tags = response.data
        },

        checkId(item) {
            console.log(`ID: ${item}`)
        }
    },

    
}
</script>

<style>

</style>