<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div>
      <h2>예약</h2>
      <a v-for="(time, index) in timesList" :key="index">
        
        <span>{{ time }}</span>
      </a>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data: function () {
    return {
      timesList: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      timeClicked: [],
      timeTable: ["00:00",],
    }
  },
    // 각 타임 테이블 클릭할 때, 해당 테이블의 idx를 timeClicked에 넣는다.
  methods: {
    timeClick (idx) {
      // timeClicked의 길이가 5 미만일 때만 클릭시 로직에 들어간다. 
      if (length(this.timeClicked) < 5) {
        // 이미 클릭 된 개체라면, 리스트에서 제거해누고
        if (idx in this.timeClicked) {
          this.timeClicked
        } 
        // 아니라면 리스트에 넣어주는 로직으로 진행한다.
        else {

        }
        
      } else {
      }
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
