<template>

  <div class="nav-header">
    <div class="content">
      <div class="nav-title">全友全屋定制</div>
      <nav-btn @toggleNav="toggle"></nav-btn>
    </div>
    <nav-detail  class="nav-detail" :show="show"></nav-detail>
  </div>

</template>

<script>
import navBtn from '@/components/base/nav-btn'
import navDetail from '@/components/base/nav-detail'
export default {
  data () {
    return {
      show: false
    }
  },
  components:{
    navBtn,
    navDetail
  },
  methods: {
    toggle (status) {
      this.show = status
    }
  }
}
</script>

<style lang="stylus" scoped>
.nav-header
  position fixed
  z-index 200
  top 0
  left 0
  right 0
  .content
    position fixed
    top 0
    left 0
    width 100%
    z-index 2
    height 100%
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
</style>