<template>

  <scroll class="index">
    <div>
      <index-swiper class="index-swiper"></index-swiper>
      <index-order></index-order>
      <div class="mask"></div>
      <a class="banner1" href="#"></a>
    </div>
  </scroll>

</template>

<script>
import Scroll from '@/components/scroll'
import indexSwiper from '@/components/index-swiper'
import indexOrder from '@/components/index-order'

export default {
  // components: {
  //   Logo
  // }
  components: {
    indexSwiper,
    indexOrder,
    Scroll
  }
}
</script>

<style lang="stylus" scoped>
.index
  position absolute
  top 80px
  right 0
  left 0
  bottom 0
  .mask
    height 0
    width 100%
    padding-bottom 16%
  .container
    width 500px
  .index-swiper
    margin-top 20px  
  .banner1
    display block
    height 0
    width 100%
    padding-bottom 36.8%
    background-image url("~@/assets/images/home/banner1.jpg")
    background-repeat  no-repeat
    background-size 100% 100%
</style>