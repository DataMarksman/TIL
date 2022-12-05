<template>
  <div>
    <li class="list-group-item video-item" @click="pickOne">
      <img :src="videoImgUrl" alt="thumbnail">
      <div>{{ video.snippet.title }}</div>
    </li>
    
  </div>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: Object,
  },
  methods: {
    pickOne() {
      this.$emit('select', this.video)
    }
  },
  computed: {
    videoImgUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>
  .video-item {
    display: flex;
    cursor: pointer;
  }
</style>