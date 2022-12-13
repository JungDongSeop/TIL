<template>
  <div id="app">
    <h1>App</h1>
    <input 
      type="text" 
      :value="appData"
      @input="event => appData = event.target.value"
    >
    <p>parrentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>

    <AppParent 
      :app-data="appData" 
      @give-parent-data="giveParentData"
      @give-child-data="giveChildData"
    />

  </div>
</template>

<script>
import AppParent from '@/components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data() {
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods: {
    getAppData(inputData) {
      this.appData = inputData
    },
    giveParentData(inputData) {
      this.parentData = inputData
    },
    giveChildData(inputData) {
      this.childData = inputData
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
</style>
