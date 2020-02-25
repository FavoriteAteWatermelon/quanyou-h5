<template>
  <div class="index-swiper">
    <div  v-show="isLoaded" v-swiper:mySwiper="swiperOption"    >
        <div class="swiper-wrapper">
        <img class="swiper-slide" @load="add" src="@/assets/images/home/swiper1.jpg" alt="">
        <img class="swiper-slide" @load="add" src="@/assets/images/home/swiper2.jpg" alt="">
        <img class="swiper-slide" @load="add" src="@/assets/images/home/swiper3.jpg" alt="">
        </div>
        <div v-show="isLoaded" class="swiper-pagination"></div>
    </div>
    <div class="default-logo" v-show="!isLoaded" >
    </div>
  </div>
</template>

<script>
export default {
  
  data () {
    return {
      isLoaded: false,
      loadImgNumber: 0,
      num:3,
      swiperOption: {
        slidesPerView :1,
        // direction:'',
        autoplay: {
            delay: 2500,
            disableOnInteraction: false
        },
          pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        height:100,
        spaceBetween : 10,
        loop: true,
        pagination: {
            el: '.swiper-pagination'
        },
        
      }
    }
},
methods: {
  add() {
    if (this.loadImgNumber < 2) {
      this.loadImgNumber ++
    } else {
      this.$nextTick(() => {
        this.loadImgNumber = 0
        this.isLoaded = true
      })
    }
  }
}
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/common/stylus/variable'
>>>.swiper-pagination-bullet-active
  background $color-theme
// >>>.swiper-pagination-bullet
//   background #fff
//   opacity 0.2 
.swiper-wrapper
  width 100%
  img
    width 100%
.default-logo
  width 100%
  height 0
  padding-bottom 42.6%
  background url('~@/assets/images/common/default.png') center no-repeat
</style>