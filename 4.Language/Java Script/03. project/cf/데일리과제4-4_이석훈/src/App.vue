<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <button @click="clickHome">Home</button>
    <button @click="clickStart">Start</button>
    <div>
      <Home v-if="!isStarted&&page==1"/>
      <Nocolor v-if="isStarted&&page===1" 
      @click-left="isleftClicked"
      @click-right="isRightClicked"
       :page="page"/>
      <Ssafling v-if="isStarted&&page===2" 
            @click-left="isleftClicked"
      @click-right="isRightClicked"
      :page="page"/>
      <Ssafleaf v-if="isStarted&&page===3" 
            @click-left="isleftClicked"
      @click-right="isRightClicked"
      :page="page"/>
      <Ssaflower v-if="isStarted&&page===4" 
            @click-left="isleftClicked"
      @click-right="isRightClicked"
      :page="page"/>
    </div>
  </div>
</template>

<script>
import Home from '@/components/Home'
import Nocolor from '@/components/Nocolor'
import Ssafleaf from '@/components/Ssafleaf'
import Ssafling from '@/components/Ssafling'
import Ssaflower from '@/components/Ssaflower'


export default {
  name: 'App',
  components: {
    Home,
    Nocolor,
    Ssafleaf,
    Ssafling,
    Ssaflower,
  },
  data : function() {
    return {
      page : 1,
      isStarted : false,
    }
  },
  methods:{
      clickHome:function(){
        this.isStarted=false
        this.page=1
      
    },
    clickStart:function(){
      this.isStarted=true
    },
    isleftClicked:function(nowPage){
      this.page=nowPage[0]
      this.isStarted=nowPage[1]
    },
    isRightClicked:function(nowPage){
      if(this.page==4){
        alert("Home으로 돌아갑니다!")
        this.page=nowPage[0]
        this.isStarted=nowPage[1]
      }else{
        this.page=nowPage[0]
        this.isStarted=nowPage[1]
      }
      
    }
  }
}
</script>

<style>

</style>
