<template>
  <div id="app">
    <h3 ref="appText">{{ text }}</h3>
    <button @click="increase">Update Data</button>
    <h3 ref="appNumber">{{ number }}</h3>
    <hr>
    <button @click="toggleIsActive">Toggle ChildItem</button>
    <ChildItem v-if="isActive"/>
  </div>
</template>

<script>
import ChildItem from '@/components/ChildItem'

export default {
  name: 'App',
  components: {
    ChildItem
  },
  data() {
    return {
      text: '초기 데이터',
      number: 0,
      isActive: false
    }
  },
  methods: {
    increase() {
      this.number++
    },
    toggleIsActive() {
      this.isActive = !this.isActive
    }
  },
  // lifecycle hooks 순서
    // Create 이전이라 this.text에 접근도 불가능
  beforeCreate() {
    console.log('---- beforeCreate App.vue ---')
    console.log(`this.text 호출 ${this.text}`)
    this.text = 'App.vue가 beforeCreated 된 시점'
    alert(this.text)
  },
  created() {
    console.clear() // beforeCreate에서 호출한 console 정리
    console.log('---- created App.vue ----')
    this.text = 'App.vue가 created 된 시점'   // data 접근 가능
    console.log(this.text)

    this.increase()   // method 호출도 정상 작동
    console.log(this.$refs.appText)   // DOM 접근 불가능. (mount 전)
    alert(this.text)
  },
  beforeMount() {
    // mount 되기 직전에 호출
    console.clear()
    console.log('---- beforeMount App.vue ----')
    console.log(this.$refs.appText)     // 아직 접근 불가능
  },
  mounted() {
    // console.clear()
    console.log('---- mounted App.vue ----')
    console.log(this. $refs.appText)    // DOM 접근 가능
    this.text ='App.vue가 mounted 된 시점'
    alert(this.text)
  },
  beforeUpdate() {
    console.log('---- beforeUpdate App.vue ----')
  },
  updated() {
    console.log('---- updated App.vue ----')
    console.log(this.isActive)
    // this.number++   이거 실행하면 무한반복. 서버 터짐
  },

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
