<template>
  <div 
    class="search-bar"
    :style="{ margin: videoLength ? '0' : '40vh 0' }"
  >
    <input 
      type="text"
      v-on:keydown.enter="onInputKeyword"
    >
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  props: {
    videoLength: Number
  },
  methods: {
    onInputKeyword: function(event) {
      // console.log(event.target.value)
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>
.search-bar > input {
  width: 100%;
  padding: 0.5rem;
  font-size: 2rem;
}

.search-bar {
  transition-duration: 10s;
}

</style>