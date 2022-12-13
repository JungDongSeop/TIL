<template>
  <div>
    <ul class="list-group">
      <VideoListItem
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @select-video="onSelectVideo"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videos: Array
  },
  methods: {
    onSelectVideo(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>