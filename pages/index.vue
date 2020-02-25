<template>

  <scroll class="index">
    <div>
      <index-swiper class="index-swiper"></index-swiper>
      <index-order></index-order>
      <h1>dfdfadf</h1>
      <h1>dfdfadf</h1>
      <h1>dfdfadf</h1>
      <h1>dfdfadf</h1>
      <h1>dfdfadf</h1>
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
  .container
    width 500px
  .index-swiper
    margin-top 20px  
</style>