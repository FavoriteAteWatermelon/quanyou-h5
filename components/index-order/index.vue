<template>
  <div class="index-order">
    <img class="banner" src="@/assets/images/home/limitTime.png" alt="">
    <img class="features"  src="@/assets/images/home/features.png" alt="">
    <el-form  class="order-form">
      <div class="order-info">
        <el-input placeholder="姓名"  class="order-name" v-model="form.name"></el-input>
        <el-input placeholder="电话" type="number" class="order-tel" v-model="form.tel"></el-input>
      </div>
      <area-select></area-select>
       <el-input placeholder="详细地址"  class="order-address" v-model="form.address"></el-input>
       <el-button class="submit-btn" @click="submitForm('form')">马上预约</el-button>
       <div class="enjoy">享受0元设计</div>
      <!-- <el-form-item label="活动名称">
      </el-form-item> -->
    </el-form>
  </div>
</template>

<script>
import areaSelect from '@/components/base/area-select'
export default {
  data () {
    return {
      form: {
        name : '',
        tel: '',
        address: ''
      }
    }
  },
  created () {
  },
  methods: {
  },
  components: {
    areaSelect
  }
  
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/common/stylus/variable'
.index-order
  margin 50px 5% 0 5%
  border-radius 5px
  background $color-theme
  .banner
    margin -40px 0 0 10%
    width 80%
  .features
    margin 10px 0 0 10%
    width 80%
  .order-form
    .order-info
      display flex
      justify-content space-around
      margin-top 10px
      .order-name,.order-tel
        width 40%
    .order-address
      width 90%
      margin 0 5%
  >>>.submit-btn
    background #0b8564
    color #ffffff
    width 90%
    margin 15px 5%
    font-size 20px
    font-weight bold
  .enjoy
    position relative
    padding-bottom 20px
    color #fff
    height 20px
    width 100%
    text-align center
    font-size 16px
    text-align center
    &::before
      position absolute
      left 5%
      top 9px
      content ''
      height 2px
      width 25%
      line-height 20px
      background #fff
      border-radius 4px
    &::after
      position absolute
      right 5%
      top 9px
      content ''
      height 2px
      width 25%
      line-height 20px
      background #fff
      border-radius 4px
</style>