<template>
  <div class="whole-house-wrapper">
    <div class="whole-house-title">
      <div class="house-title">{{title}}</div>
      <div class="house-subtitle">{{subTitle}}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '全友家私'
    },
    subTitle: {
      type: String,
      default: 'quanyou'
    }
  }
  
}
</script>

<style lang="stylus" scoped>
  .whole-house-wrapper
    background #f5f5f5
    padding-top 20px
    text-align center
    padding-bottom 30px
    .house-title
      font-size 20px
    .house-subtitle
      margin-top 10px
      font-size 14px
      color #666
</style>