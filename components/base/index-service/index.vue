<template>
  <div class="service">
    <div class="left">
      <div class="logo">
        <img :src="imgUrl" alt="">
      </div>
      <div class="subTitle">{{subTitle}}</div>
      <div class="title">{{title}}</div>
    </div>
    <div class="right">
      <ul>
        <li v-for="(item,index) in infoDetail" :key="index">{{item}}</li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      imgUrl: {
        type: String,
        default: {}
      },
      subTitle: {
        type: String,
        default: ''
      },
      title: {
        type: String,
        default: ''
      },
      infoDetail: {
        type: Array,
        default: []
      }
    }
    
  }
</script>

<style lang="stylus" scoped>
.service
  display flex
  background #258566
  color #fff
  padding 20px 0
  .left
    flex 1
    height 108px
    text-align center
    border-right 1px  solid #fff
    .subTitle
      opacity 0.6
      font-size 12px
      margin 10px 0
    .logo
      img
        width 45px
  .right
    height 108px
    flex 1
    display table
    text-align center
    ul
      display table-cell
      vertical-align middle 
      li
        margin-bottom 10px    
</style>