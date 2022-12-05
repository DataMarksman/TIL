<template>
  <div>
    <h3>난 My Compo의 하위 컴포야~</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent"> 클릭! </button>
  </div>
</template>

<script>

export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  methods: {
    childToParent: function() {
      this.$emit('cry-baby')
    }

  }
}
</script>

<style>
  
</style>