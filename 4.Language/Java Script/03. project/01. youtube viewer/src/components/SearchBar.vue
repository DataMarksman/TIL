<template>
  <div >
    <input type="text" v-model="query">
    <button class="btn btn-primary" @click="onSearch">검색</button>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY


export default {
  name: "SearchBar",
  data() {
    return {
      query: '',
    }
  },
  methods: {
    onSearch() {
      axios.get(URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: this.query,

        }
      })
        .then(res => this.$emit('fetch-videos' ,res.data.items))
    }
  }

}
</script>

<style>

</style>