<template>
  <div id="app" class="container vuetube-wrap ">
    <!-- 제목 영역 -->
    <header class="d-felx justify-content-center">
      <h1 class="'mt-4 text-primary">SSAFY TUBE</h1>
    </header>

    <!-- 검색바 -->
    <SearchBar @fetch-videos='onFetchVideos'/>

    <!-- 본문 -->
    <section class="row mt-4">
      <!-- 비디오 플레이어 영역 -->
      <div class="mt-4">
        <VideoDetail :selectedVideo="selectedVideo" />
      </div>
      <!-- 비디오 리스트 영역 (5개) -->
      <div>
        <VideoList :videos="videos" @select="onSelect" />
      </div>

    </section>
  </div>
</template>


<!-- APP.vue: 특정 하나의 비디오 정보, 비디오 리스트 가짐  -->
<!-- VideoDetail 에서 비디오 하나, 다 -->
 
<script>
// 스크립트 작성 순서: import -> 명시 -> 사용
import SearchBar from '@/components/SearchBar.vue'
import VideoDetail from '@/components/VideoDetail.vue'
import VideoList from '@/components/VideoList.vue'
// import axios from 'axios'

export default {
  name: 'App',
  
  components: {
    SearchBar, VideoDetail, VideoList
  },
  data() {
    return {
      videos: [],
      selectedVideo: {},
    }
  },
  methods: {
    onFetchVideos(videos) {
      this.videos = videos
    },
    onSelect(selectedVideo) {
      this.selectedVideo = selectedVideo
    }
  },
  computed: {
    isSelectedVideo() {
      return !!Object.keys(this.selectedVideo).length
    }
  }
}
</script>

<style>
  .vuetube-wrap {
    min-height: 100vh;
  }
</style>
