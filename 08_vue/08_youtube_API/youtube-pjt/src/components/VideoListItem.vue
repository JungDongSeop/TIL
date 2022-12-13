<template>
  <li class="list-group-item" @click="selectVideo">
    <img 
      :src="thumbnailImgUrl"
    >
    <!-- <p v-html="video.snippet.title"></p> -->
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    thumbnailImgUrl() {
      return this.video.snippet.thumbnails.default.url
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
.list-group-item {
  display: flex;
  cursor: pointer;
}

.list-group-item:hover {
  background-color: #eee;
}

.list-group-item img {
  height: fit-content;
  margin-right: 0.5rem;
}

</style>