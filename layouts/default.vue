<template>
  <div class="layout">
    <div class="nav-header">
      <div class="nav-title">全友全屋定制</div>
      <nav-btn></nav-btn>
    </div>
    <nuxt/>

  </div>
</template>

<script>
import navBtn from '@/components/base/nav-btn'
export default {
  components:{
    navBtn
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
  .nav-header
    position fixed
    z-index 200
    top 0
    left 0
    right 0
    display flex
    justify-content space-between
    box-sizing border-box
    padding 0 10px
    height 50px
    background #fff
    box-shadow 2px 2px 10px rgba(0,0,0,.1)
    .nav-title
      line-height 50px
      font-size 20px
      font-weight 800
      letter-spacing 1px
      cursor pointer
  .con
    position absolute
    top 50px
    right 0
    left 0
    bottom 0
    overflow hidden
</style>
