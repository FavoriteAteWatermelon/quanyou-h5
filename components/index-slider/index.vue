<template>
  <div class="index-slider" ref="slider">
    <div class="slider-group" ref="sliderGroup">
      <slot></slot>
    </div>
    <slider-dots :showDots="showDots" :isTransition="isTransition" :currentPageIndex="currentPageIndex" :dots="dots"></slider-dots>
  </div>
</template>

<script>
import BScroll from 'better-scroll'
import {addClass} from '@/assets/js/dom'
import sliderDots from '@/components/base/slider-dots'
export default {
  props: {
    loop: {
      type: Boolean,
      default: true
    },
    autoPlay: {
      type: Boolean,
      default: true
    },
    interval: {
      type: Number,
      default: 4000
    },
    isTransition: {
      type: Boolean,
      default: true
    },
    showDots: {
      type: Boolean,
      default: true
    }
  },
  mounted () {
    setTimeout (() => {
      this._setSliderWidth()
      this._initDots()
      this._initSlider()
      this.$emit('dotsStatus', [this.dots, this.currentPageIndex])
      if (this.autoPlay) {
        this._play()
      }
    }, 20)
  },
  data () {
    return {
      dots: [

      ],
      currentPageIndex: 0
    }
},
components: {
  sliderDots
},
methods: {
  _setSliderWidth () {
    this.children = this.$refs.sliderGroup.children
    let width = 0
    let sliderWidth = this.$refs.slider.clientWidth
    for (let i = 0; i < this.children.length; i++) {
      let child = this.children[i]
      addClass(child,'slider-item')
      child.style.width = sliderWidth + 'px'
      width += sliderWidth
    }
    if (this.loop) {
      width += 2 * sliderWidth
    }
    this.$refs.sliderGroup.style.width = width + 'px'
  },
  _initSlider () {
    this.slider = new BScroll(this.$refs.slider, {
      scrollX: true,
      scrollY: false,
      momentum: false,
      snap: {
        loop: this.loop,
        threshold: 0.3,
        speed: 400
      }
    })
    this.slider.on('scrollEnd', () => {
      let pageIndex = this.slider.getCurrentPage().pageX
      this.currentPageIndex = pageIndex
      this.$emit('dotsStatus', [this.dots, this.currentPageIndex])
      if (this.autoPlay) {
        clearTimeout(this.timer)
        this._play()
      }
    })
  },
  _initDots () {
    this.dots = new Array(this.children.length)
  },
  _play () {
    let pageIndex = this.currentPageIndex + 1
    this.timer = setTimeout(() => {
      this.slider.next()
    },this.interval)
  }
}
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/common/stylus/variable'
.index-slider
  position relative
  min-height 1px
  overflow-x hidden
  .slider-group
    position relative
    overflow hidden
    white-space nowrap
    .slider-item
      float left
      box-sizing border-box
      overflow hidden
      text-align center
      a
        display block
        width 100%
        overflow hidden
        text-decoration none
        img
          display: block
          width: 100%
  // background url('~@/assets/images/common/default.png') center no-repeat
</style>