<template>
  <div class="nav-detail" :class="{'isShow' : show}">
    <div class="nav-title"></div>
    <ul>
      <li class="nav-item">热销产品</li>
      <li class="nav-item">0元设计</li>
      <li class="nav-item">空间分类</li>
      <li class="nav-item">全屋定制</li>
      <li class="nav-item">预约设计师</li>
      <li class="nav-item">家居DIY</li>
      <li class="nav-item">门店查询</li>
      <li class="nav-item">售后服务</li>
      <li class="nav-item">最新资讯</li>
      <li class="nav-item">全屋案例资讯</li>
    </ul>
    <div class="contact">
      <div class="qrcode">
        <img src="" alt="">
        <div class="description"></div>
      </div>
      <div class="tel">
        <div class="tel-title"></div>
        <div class="tel1"></div>
        <div class="tel1"></div>
        <div class="email"></div>
      </div>
    </div>
    <div class="service">
      <div class="home">全友家居</div>
      <div class="bache">全友卫浴</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style lang="stylus" scoped>
.nav-detail
  position fixed
  top 50px
  bottom 0
  left 0
  right 0
  transition all 1s
  transform  translateY(-100%)
  opacity 0
.isShow
  opacity 1
  transform translateY(0)  
</style>