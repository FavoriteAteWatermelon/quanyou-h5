<template>

  <scroll class="index">
    <div>
      <div class="slider-wrappper">
        <indexSlider class="index-slider">
          <div class="slider-item" v-for="item in sliderMain" :key="item">
             <a href=""><img  :src="item" alt=""></a>
          </div>
        </indexSlider>
      </div>
      <index-order></index-order>
      <div class="mask"></div>
      <a class="banner1" href="#"></a>
      <indexHouseInfo></indexHouseInfo>
      <div class="slider-title-wrapper">
        <indexSlider  @dotsStatus="dotsStatus" :showDots="sliderTitle.showDots" :autoPlay="sliderTitle.autoPlay" :title="sliderTitle.title" :isTransition="sliderTitle.isTransition">
          <div class="slider-item" v-for="(item, index) in sliderTitle.images" :key="item">
             <a href="">
               <img  :src="item" alt="">
               <div class="name">
                 {{sliderTitle.titles[index]}}
               </div>
              </a>
          </div> 
        </indexSlider>
      </div>
      <div class="patch-bottom">
        <sliderDots :isTransition="patch.isTransition" :dots="patch.dots" :currentPageIndex="patch.activeIndex"> </sliderDots>
      </div>  
    </div>
  </scroll>

</template>

<script>
import scroll from '@/components/scroll'
import indexSlider from '@/components/index-slider'
import indexOrder from '@/components/index-order'
import indexHouseInfo from '@/components/index-house-info'
import sliderDots from '@/components/base/slider-dots'


export default {
  data () {
    return {

      sliderMain: [
        require('@/assets/images/home/swiper1.png'),
        require('@/assets/images/home/swiper2.png'),
        require('@/assets/images/home/swiper3.png'),
      ],

      patch: {
        dots: [],
        activeIndex: 0,
        isTransition: false
      },
      sliderTitle:{
        autoPlay: false,
        title: true,
        showDots: false,
        images:  [
        require('@/assets/images/home/title1.jpg'),
        require('@/assets/images/home/title2.jpg'),
        require('@/assets/images/home/title3.jpg'),
        require('@/assets/images/home/title4.png'),
        require('@/assets/images/home/title5.jpg'),
        require('@/assets/images/home/title6.png')
        ],
        titles: [
          '红遍朋友圈的全屋定制设计，99%的女人都想要！',
          '6个爆款衣帽间，每个设计都值得借鉴！',
          '家里这样设计，亲朋好友来串门从头夸到尾',
          '看好了！这样装玄关，让你家功能颜值+10倍！',
          '超实用的8个收纳技巧，春节亲戚来玩，全靠它“撑场面”',
          '小户型的逆袭——小餐厅的9种巧妙设计！'
        ]
      }
    }
  },
  components: {
    indexSlider,
    indexOrder,
    scroll,
    indexHouseInfo,
    sliderDots
  },
  methods: {
    dotsStatus (status) {
      this.patch.dots = status[0]
      this.patch.activeIndex = status[1]
    }
  }
}
</script>

<style lang="stylus" scoped>
.index
  position absolute
  top 80px
  right 0
  left 0
  bottom 0
  .slider-wrappper
    height 0
    padding-bottom 42.6%
    width 100%
    overflow hidden
  .mask
    height 0
    width 100%
    padding-bottom 16%
  .container
    width 500px
  .index-swiper
    margin-top 20px  
  .banner1
    display block
    height 0
    width 100%
    padding-bottom 36.8%
    background-image url("~@/assets/images/home/banner1.jpg")
    background-repeat  no-repeat
    background-size 100% 100%
  .slider-title-wrapper
    height 0
    padding-bottom 39.73%
    width 100%
    .name
      height 20px
      line-height 20px
      background #fff
      font-size 14px
      color #3e3e3e
    // overflow hidden
  .patch-bottom
    height 60px
    width 100%
    background #f5f5f5

    // z-index -1
    // margin-bottom 100px  
</style>