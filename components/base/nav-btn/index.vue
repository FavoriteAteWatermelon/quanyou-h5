<template>
  <div class="nav-btn" @click="isRotate">
    <div class="cube">
      <div class="line1" :class="{'active1': isActive}"></div>
      <div class="line2" :class="{'active2': isActive}"></div>
      <div class="line3" :class="{'active3': isActive}"></div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isActive: false
    }
  },
  methods: {
    isRotate () {
      this.isActive ? this.isActive = false : this.isActive = true
      this.$emit('toggleNav', this.isActive)
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/common/stylus/variable'
.nav-btn
  width 50px
  height 50px
  display flex
  justify-content center
  align-items center
  cursor pointer
  .cube
    position relative
    display flex
    flex-direction column
    align-items center
    height 28px
    width 28px
    .line1
      position absolute
      top 0
      width 28px
      height 3px
      background $color-theme
      border-radius 5px
      transition all 0.5s cubic-bezier(.5,-0.21,.52,1.11)
    .line2
      position absolute
      top 12.5px
      width 28px
      height 3px
      background $color-theme
      border-radius 5px
      transition all 0.3s ease-in-out
    .line3
      position absolute
      top 25px
      width 28px
      height 3px
      background $color-theme
      border-radius 5px
      transition all 0.5s cubic-bezier(.5,-0.21,.52,1.11)
    .active1
      top 12.5px
      transform rotate(135deg)
    .active2
      opacity 0
    .active3
      top 12.5px
      transform rotate(-135deg)
</style>