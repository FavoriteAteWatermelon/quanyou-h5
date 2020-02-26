<template>
  <div class="layout">
    <nav-header></nav-header>
    <nuxt/>
  </div>
</template>

<script>
import navHeader from '@/components/nav-header'
export default {
  components:{
    navHeader
  }
  
}
</script>

<style lang="stylus" >
@import "~@/assets/common/stylus/index.styl";
.layout
  position absolute
  top 0
  left 0
  right 0
  bottom 0
  // overflow hidden
</style>
