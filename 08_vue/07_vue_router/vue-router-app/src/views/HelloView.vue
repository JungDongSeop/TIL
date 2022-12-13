<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloView',
  data() {
    return {
      userName: this.$route.params.userName
    }
  },
  // 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
  beforeRouteUpdate(to, from, next) {
    // 파라미터의 변화를 감지시킴
    this.userName = to.params.userName
    next()
  }
}
</script>

<style>

</style>