<template>
  <div class="index">
    <index-swiper></index-swiper>
    <index-order></index-order>
  </div>
</template>

<script>
import indexSwiper from '@/components/index-swiper'
import indexOrder from '@/components/index-order'

export default {
  // components: {
  //   Logo
  // }
  components: {
    indexSwiper,
    indexOrder
  }
}
</script>

<style lang="stylus" scoped>
.container
  width 500px
</style>