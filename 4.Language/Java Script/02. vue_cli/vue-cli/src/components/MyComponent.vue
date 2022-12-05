<template>
  <div class="border">
    <h1>내가 만든 새로운 컴퍼넌트얍</h1>
    <MyComponentItem
      static-props="MyComponent에서 보낸 데이터"
        :dynamic-props = "dynamicProps"
        @cry-baby="parentGetEvent"
      />
  </div>
</template>

<script>
// 1. 불러오기 -> 안쓰면 에러난다구?
import MyComponentItem from '@/components/MyComponentItem';

export default {
  name: 'MyComponent',
  components: {
    // 2. 등록해주기~ -> 하지만 이 이후에 안쓰면 또 에러 뜬다구?
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: "이건 동적인 데이터!"
    }
  },
  methods: {
    parentGetEvent: function() {
      console.log("No Money!")
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>