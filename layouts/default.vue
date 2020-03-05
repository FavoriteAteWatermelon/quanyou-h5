<template>
  <div class="layout">
    <nav-header></nav-header>
    <online></online>
    <nuxt/>
  </div>
</template>

<script>
import navHeader from '@/components/nav-header'
import online from '@/components/online'
export default {
  components:{
    navHeader,
    online
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
