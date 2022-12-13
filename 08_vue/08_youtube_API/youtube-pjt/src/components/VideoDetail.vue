<template>
  <div v-if="video" class="video-detail">
    <div class="video-container">
      <iframe 
        :src="videoURL" frameborder="0"
      >
      </iframe>
    </div>

    <div class="video-detail__text">
      <h2>{{ video.snippet.title | stringUnescape }}</h2>
      <p>{{ video.snippet.description | stringUnescape }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: Object
  },
  computed: {
    videoURL() {
      // const videoId = this.video.id.videoId
      const { videoId } = this.video.id
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape(rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
.video-detail {
  width: 113.45%;
  padding-right: 1rem;
}

.video-container {
  position: relative;
  padding-top: 56.25%;
}

.video-container > iframe {
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
}

.video-detail__text {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid lightgray;
  border-radius: 10px;
}

</style>