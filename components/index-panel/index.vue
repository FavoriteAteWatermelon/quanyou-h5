<template>
  <div class="custom-style">
    <index-title :title="title" :subTitle="subTitle"></index-title>
    <div class="house-style-image-wrapper">
      <div v-for=" (item, index) in gallery" :key="index"  class="image-item">
        <img :src="item.url" alt="">
        <div class="title">{{item.title}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import indexTitle from '@/components/base/index-title'
export default {
  props: {
    title: {
      type: String,
      default: '全友家私'
    },
    subTitle: {
      type: String,
      default: 'quanyoujiasi'
    },
    gallery:{
      type: Array,
      default: () => {
        return [
        {
        title: '',
        url: ''
      }]
      }
    },
  },
  components : {
    indexTitle
  }
}
</script>

<style lang="stylus" scoped>
.custom-style
  background #f5f5f5
  .house-style-image-wrapper
    display flex
    flex-wrap wrap
    .title
      height 30px
      line-height 30px
      background #fff
    .image-item
      box-sizing border-box
      width 50%
      text-align center
      color #3e3e3e
      font-size 14px
      img
        margin 5%
        width 90%
</style>