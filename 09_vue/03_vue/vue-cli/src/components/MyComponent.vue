<template>
  <div class="border">
    <h1>내가 만든 새로운 컴포넌트</h1>    
    <MyComponentItem 
    static-props="MyComponent에서 보낸 데이터"
    :dynamic-props="dynamicProps"
    @show-me-the-money="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  // 이름을 설정해야 해당 vue 파일에 접근 가능
  // 그래서 일반적으로 파일명과 동일한 이름으로 설정
  name: 'MyComponent',
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  // scope 범위 때문에 함수로 정의
  data: function () {
    return{
      dynamicProps: '이건 동적인 데이터'
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log('용돈 없어!!')
      console.log(childData)
    },
    getDynamicData: function (childInput) {
    console.log(`사용자가 입력한 값은 ${childInput}임니다.`)
    }
  },

}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>