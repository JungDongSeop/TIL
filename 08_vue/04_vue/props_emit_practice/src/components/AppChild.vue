<template>
  <div>
    <h1>AppChild</h1>
    <input 
      type="text"
      :value="childData"
      @input="event => {
        childData = event.target.value
        giveChildData()
      }"
    >
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: "AppChild",
  props: {
    appData: String,
    parentData: String,
  },
  data() {
    return {
      childData: null
    }
  },
  methods: {
    giveChildData() {
      this.$emit('give-child-data', this.childData)
    }
  }
}
</script>

<style>

</style>