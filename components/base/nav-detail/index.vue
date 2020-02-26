<template>
  <div class="nav-detail" :class="{'isShow' : show}">
    <div class="nav-title">
      首页
    </div>
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
    <div class="about-us">
      <div class="contact" >
        <div class="qrcode" :class="{'active-us' : show}">
          <img src="@/assets/images/common/qrcode.jpg" alt="">
          <a href="#">关注获取更多</a>
        </div>
        <div  class="tel" :class="{'active-us' : show}">
          <div class="tel-title">统一热线:400-8800-315</div>
          <a href="tel:86-28-66771818">86-28-66771818</a>
          <a href="tel:86-28-66771818">86-28-66771818</a>
          <div class="email">EAMIL:kf@quanyou.com</div>
        </div>
      </div>
      <div class="service">
        <div class="home">
          <a href="">全友家居</a> 
          </div>
        <div class="bache">
          <a href="">全友卫浴</a>
        </div>
      </div>
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
  transition all 10s
  transform  translateY(-100%)
  opacity 0
  background #fff
.isShow
  opacity 1
  transform translateY(0)
  .nav-title
    height 50px
    width 100%
    box-sizing border-box
    padding-left 20px
    font-size 20px
    color #fff
    font-weight bold
    line-height 50px
    background-image url("~@/assets/images/common/detail_bg.jpg")
  ul
    display flex
    flex-wrap wrap
    li
      box-sizing border-box
      line-height 50px
      text-align center
      width 50%
      height 50px
      font-weight bold
      border 1px solid #eee
  .about-us
    position absolute
    bottom 0
    left 0
    right 0
    height 220px
    .contact
      display flex
      height 120px
      justify-content space-around
      .qrcode
        transition all 10s
        transform translateX(-200px)
        display flex
        flex-direction column
        justify-content space-between
      .tel
        transition all 10s
        transform translateX(200px)
        display flex
        flex-direction column
        justify-content space-between
      .active-us
        transform translateX(0)
        opacity 1   
  .service
    display flex
    justify-content space-between
    height 70px
    line-height 70px
    margin-top 30px
    border-top 1px solid #eee
    div
     flex 1
     display flex
     justify-content center
     align-items center
     border-right  1px solid #eee
     a
       display block
       height 30px
       line-height 30px
       width 100px
       border-radius 5px
       font-size 16px
       text-align center
       border 1px solid #3dc094

</style>