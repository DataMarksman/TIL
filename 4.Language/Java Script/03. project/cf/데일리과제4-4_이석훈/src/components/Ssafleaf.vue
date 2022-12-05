<template>
  <div>
    <img src="../assets/ssafleaf.png" alt="">
    <button @click="clickLeft" >왼쪽</button>
    <button @click="clickRight" >오른쪽</button>
  </div>
</template>

<script>
export default {
  'name': 'Ssafleaf',
  methods:{
  clickLeft:function(){
    this.$emit('click-left',
    this.page==1?[this.page,false]:[this.page-1,true]
    )
  },
    clickRight:function(){
    this.$emit('click-right',
    this.page==4?[1,false]:[this.page+1,true]
    )
  },
  },
  props:{
    page:Number,
  }
}
</script>

<style>

</style>