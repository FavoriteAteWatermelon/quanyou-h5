<template>
  <div class="online">
    <div>
      <div>在线</div>
      <div>咨询</div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style lang="stylus" scoped>
.online
  position fixed
  bottom 100px
  right 30px
  box-sizing border-box
  width 35px
  height 35px
  line-height 12.5px
  text-align center
  font-size 12px
  border-radius 50%
  color #fff
  background #f35321
  z-index 200
  cursor pointer
  box-shadow: 0 0 20px rgba(0,0,0,.2);
  &>div
    margin-top 5.5px
  // background 
</style>