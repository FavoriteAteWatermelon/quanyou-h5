<template>
  <div>
    <div class="slider-title-wrapper">
      <indexSlider  :showDots="sliderTitle.showDots" :autoPlay="sliderTitle.autoPlay" :title="sliderTitle.title" :isTransition="sliderTitle.isTransition">
        <div class="slider-item" v-for="(item, index) in sliderTitle.images" :key="item">
            <a href="">
              <img  :src="item" alt="">
              <div class="name">
                {{sliderTitle.titles[index]}}
              </div>
            </a>
        </div> 
      </indexSlider>
    </div>
    <div class="patch-bottom">
      <sliderDots :isTransition="patch.isTransition" :dots="patch.dots" :currentPageIndex="patch.activeIndex"> </sliderDots>
    </div>
  </div>
</template>

<script>
import indexSlider from '@/components/index-slider'
import sliderDots from '@/components/base/slider-dots'
export default {
  components: {
    indexSlider,
    sliderDots
  },
  methods: {
    dotsStatus (status) {
      this.patch.dots = status[0]
      this.patch.activeIndex = status[1]
    }
  }
  
}
</script>

<style lang="stylus" scoped>

</style>