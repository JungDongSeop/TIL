<template>
  <div>
    <h1 ref="childText">{{ childText }}</h1>
  </div>
</template>

<script>
export default {
  name: 'ChildItem',
  data() {
    return {
      childText: '자식 초기 데이터',
    }
  },
  created() {
    console.log('%c   ---- created ChildItem.vue ----', "color:crimson")
  },
  mounted() {
    console.log('%c   ---- mounted ChildItem.vue ----', 'color:royalblue')
    this.childText = 'ChildItem이 mounted 된 시점'
    alert(this.childText)     // 자식 컴포넌트가 먼저 mount 되고, 이후 부모 컴포넌트가 mount
  },
    beforeDestroy() {
    // 컴포넌트가 DOM에서 제거되기 직전에 실행
    // App.vue 에서 토글 키를 끄면, childItem이 꺼지므로 실행됨
    console.log('%c   ---- beforeDestroy ChildItem.vue', 'color:green')
    this.childText = 'beforeDestroy 된 시점'
    console.log(`%c   ---- ${this.childText} ----`, 'color:orange')
    console.log(`%c   ---- ${this.$refs.childText} ----`, 'color:purple')
  },
  destroyed() {
    console.log('%c   ---- destroyed ChildItem.vue', 'color:orange')
    this.childText = 'destroyed 된 시점'
    console.log(`%c   ---- ${this.childText} ----`, 'color:orange')
    console.log(`%c   ---- ${this.$refs.childText} ----`, 'color:purple')    
  }
}
</script>

<style>

</style>