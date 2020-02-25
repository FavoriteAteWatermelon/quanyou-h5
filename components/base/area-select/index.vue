<template>
  <div class="area-select">
  <div>
   <el-select v-model="selectProvince" filterable  @change="selectProvinceFun($event)" placeholder="省份">
    <el-option value="" label="省份"></el-option>
    <el-option :value="item" :label="item.label" v-for="(item, index) in city" :key="index"></el-option>
   </el-select>
  </div>
  <div>
   <el-select v-model="selectCity" filterable @change="selectCityFun($event)" placeholder="城市">
    <el-option value="" label="城市"></el-option>
    <el-option :value="item" :label="item.label" v-for="(item, index) in cityList" :key="index"></el-option>
   </el-select>
  </div>
  <div>
   <el-select v-model="selectArea" filterable  @change="selectAreaFun($event)" placeholder="区县">
    <el-option value="" label="区县"></el-option>
    <el-option :value="item" :label="item.label" v-for="(item, index) in areaList" :key="index"></el-option>
   </el-select>
  </div>
  </div>
</template>

<script>
import city from '@/assets/json/citys.json'
export default {
  data () {
  return {
   // 整个省市县数据
   city: city,
   // 被选中的市数据
   cityList: [],
   // 被选中的县数据
   areaList: [],
   selectProvince: {},
   selectCity: {},
   selectArea: {}
  }
},
 methods: {
  // 省份 市 县联动
  selectProvinceFun (event) {
   if (event) {
    this.cityList = event.children
   } else {
    this.cityList = []
   }
   this.areaList = []
   this.$emit('getLawyerListInfo', [event.label, 'province'])
  },
  selectCityFun (event) {
   console.log(event)
   if (event) {
    this.areaList = event.children
   } else {
    this.areaList = []
   }
   this.$emit('getLawyerListInfo', [event.label, 'city'])
  },
  selectAreaFun (event) {
   console.log(event)
   this.$emit('getLawyerListInfo', [event.label, 'area'])
  }
 }
}
</script>

<style lang="stylus" scoped>
.area-select
  display flex
  margin 10px 5%
  justify-content space-between
  div
    // flex 1
    text-align center
    margin-right 5px
    // margin 10px 10px 10px 0
    &:last-child
      margin-right 0
</style>