<template>
    <div v-if="showDots" class="dots" :class="[isTransition ? 'isTransition' : '']" >
      <span :style="{background: dotBackgroundColor ? '#fffff' : '#f2f2f2' }"  :class="{active: currentPageIndex === index}" class="dot" v-for="(item,index) in dots" :key="item"></span>
    </div>
</template>

<script>
export default {
  props: {
    dots: {
      type: Array,
      default: []
    },
    isTransition: {
      type: Boolean,
      default: true
    },
    currentPageIndex: {
      type: Number,
      default: 0
    },
    dotBackgroundColor: {
      type: Boolean,
      default: true
    },
    showDots: {
      type: Boolean,
      default: true
    }
  }
  
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/common/stylus/variable'
 .dots
    position: absolute
    right: 0
    left: 0
    bottom: 12px
    transform: translateZ(1px)
    text-align: center
    font-size: 0
    .dot
      display: inline-block
      margin: 0 4px
      width: 8px
      height: 8px
      border-radius: 50%
      background: #fff
      &.active
        background: $color-theme!important
  .isTransition
    .dot
      transition all 0.4s
      &.active
        width: 20px
        border-radius: 5px
</style>