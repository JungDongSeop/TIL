<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div id="big-box">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div id='button-box'>
        <button 
          v-for="(time, index) in times" 
          :key="index"
          @click="chooseTime(time)"
          :class="{'light': !pickedTimes.includes(time), 'blue': pickedTimes.includes(time)}"
        >{{ time }}</button>
      </div>
    </div>
    
    <hr>

    <!-- <p>선택 시간 : <span v-for="(pick, index) in pickedTimes" :key="index">{{ pick }} </span></p> -->
    <p>선택 시간 : {{pickedTimes.join(' ')}} </p>


  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      pickedTimes: []
    }
  },
  methods: {
    chooseTime(time) {
      console.log(time)
      // 포함 되어 있으면, 선택 시간 리스트에 제거
      if (this.pickedTimes.includes(time)) {
        this.pickedTimes.splice(this.pickedTimes.indexOf(time), 1)
      } else if (this.pickedTimes.length === 5) {
        // 길이 5 넘으면
        alert('5타임까지만 신청할 수 있습니다.')
      } else {
        // 포함 되어 있으면, 선택 시간 리스트에 제거
        this.pickedTimes.push(time)
        this.pickedTimes.sort()
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}
#big-box {
  display: inline-block;
  box-shadow: 1px 1px 1px 1px #84898C;
}
#button-box {
  max-width: 300px;
  margin: 0 auto;
}
.light {
  background-color: white;
  color: #84898C;
  border: 0;
}
.blue {
  background-color: #658dc63d;
  border: 0;
  color: #0F4C81;
}


</style>
