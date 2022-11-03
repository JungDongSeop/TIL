<template>
  <div>
    <h1>AppParent</h1>
    <input 
      type="text"
      :value="parentData"
      @input="event => {
        parentData = event.target.value
        giveParentData()
      }"
    >
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>

    <AppChild 
      :app-data="appData" 
      :parent-data="parentData"
      @give-child-data="giveChildData"
    />

  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue'

export default {
  name: 'AppParent',
  components: {
    AppChild
  },
  data() {
    return {
      parentData: null,
      childData: null
    }
  },
  props: {
    appData: String
  },
  methods: {
    giveParentData() {
      this.$emit('give-parent-data', this.parentData)
    },
    giveChildData(inputData) {
      this.childData = inputData
      this.$emit('give-child-data', inputData)
    }


  }
}
</script>

<style>

</style>