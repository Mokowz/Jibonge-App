<template>
  <div>
    <!-- Blog Cards -->
    <div v-for="blog in blogs" :key="blog.title" class="flex justify-between px-6 py-8 border-b border-slate-500">
        <span class="text-darkGrey">{{ blog.date }}</span>

        <!-- Info -->
        <div class="flex flex-col space-y-6">
            <!-- Heading -->
            <div class="flex flex-col">
                <div class="flex flex-col">
                    <h3 class="text-3xl font-bold">{{ blog.title }}</h3>

                    <!-- Tags -->
                    <!-- <div v-for="tag in blog.tags" :key="tag" class="inline">
                        <h4 class="text-yellow-300 font-semibold inline text-xl">{{ tag }}</h4>
                    </div> -->
                    <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-300 flex font-semibold  text-xl">{{ tag }}</h4>
                </div>
                
            </div>

            <!-- Content -->
            <p class="max-w-xl text-darkGrey">{{ blog.content }}</p>

            <!-- Read More btn -->
            <a href="#">Read More</a>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            blogs: [
                {
                    'title': "First Title of My Blog",
                    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa modi magnam harum fugit saepe eaque iste quisquam reiciendis pariatur consequatur.',
                    'date': '12th April 2023',
                    'tags': ['Python', 'Football']
                },
                {
                    'title': "Second Title of My Blog",
                    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa modi magnam harum fugit saepe eaque iste quisquam reiciendis pariatur consequatur.',
                    'date': '10th June 2023',
                    'tags': ['Cartoon', 'Fun']
                }
            ],
        }
    },
}
</script>

<style>

</style>