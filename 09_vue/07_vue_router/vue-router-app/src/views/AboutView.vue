<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- 선언형 방식 네비게이션 -->
    <router-link :to="{ name: 'home' }">홈으로!</router-link>
    <!-- 프로그래밍 방식 네비게이션 -->
    <button @click="toHome">홈으로!</button>

    <!-- 입력값 받아서 HelloView로 이동 -->
    <input 
      type="text"
      v-model="inputData"
      @keyup.enter="goToHello"
    >
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home'})
    },
    goToHello() {
      this.$router.push({ name: 'hello', params: { userName: this.inputData } })
    }
  }
}
</script>
