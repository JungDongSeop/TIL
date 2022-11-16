<template>
  <div id="app">
    <h1>My First PJT</h1>
    <header>
      <TheSearchBar
        @input-change="onInputChange"
        :video-length="videos.length"
      />
    </header>

    <section>
      <VideoDetail
        :video="selectedVideo"
      />
      <VideoList
        :videos="videos"
        @select-video="onSelectVideo"
      />
    </section>
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail   
  },
  data() {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null
    }
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params
        // params: {
        //   key: API_KEY,
        //   part: 'snippet',
        //   type: 'video',
        //   q: this.inputValue
        // }
        // params: params
      })
      .then(res => {
        // console.log(res)
        this.videos = res.data.items
        this.selectedVideo = this.videos[0]
      })
      .catch(err => console.log(err))

    },
    onSelectVideo(video) {
      // console.log(video)
      this.selectedVideo = video

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

section,
header {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}

section {
  display: flex;
}
</style>
