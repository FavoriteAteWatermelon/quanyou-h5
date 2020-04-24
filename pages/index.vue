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
        <indexSlider  @dotsStatus="dotTopsStatus" :showDots="sliderTitle.showDots" :autoPlay="sliderTitle.autoPlay" :title="sliderTitle.title" :isTransition="sliderTitle.isTransition">
          <div class="slider-item" v-for="(item, index) in sliderTitle.images" :key="item">
             <a href="">
               <img  :src="item" alt="">
               <div class="name">
                 {{sliderTitle["titles"][index]}}
               </div>
              </a>
          </div> 
        </indexSlider>
      </div>
      <div class="patch-bottom">
        <sliderDots :isTransition="patch.isTransition" :dots="patch.dots" :currentPageIndex="patch.activeIndex"> </sliderDots>
      </div>
      <index-panel :title="house.title" :subTitle="house.subTitle" :gallery="house.gallery"></index-panel>
      <index-panel :title="custom.title" :subTitle="custom.subTitle" :gallery="custom.gallery"></index-panel>
      <index-panel :title="wholeHouse.title" :subTitle="wholeHouse.subTitle" :gallery="wholeHouse.gallery"></index-panel>
      <index-title :title="'设计师'" :subTitle="'DESIGNER'"></index-title>
      <div class="slider-title-wrapper-designer">
        <indexSlider :loop="false" :autoPlay="false"  @dotsStatus="dotsStatus" :showDots="sliderTitle.showDots"  :title="sliderTitle.title" :isTransition="sliderTitle.isTransition">
          <div id="designer" class="slider-item" v-for="(item, index) in galleryList" :key="index">
             
             <a href="">
               <img  :src="item[0]" alt="">
             </a>
             <a href="">
               
               <img  :src="item[1]" alt="">
              </a>
          </div> 
        </indexSlider>
      </div>
      <div class="designerStatus-patch-bottom">
        <sliderDots :dotBackgroundColor="false" :loop="designerStatus.loop" :isTransition="designerStatus.isTransition" :dots="designerStatus.dots" :currentPageIndex="designerStatus.activeIndex"> </sliderDots>
      </div>
       <index-title :title="'服务'" :subTitle="'SERVICES'"></index-title>
       <div class="service-container">
        <index-service :infoDetail="item.infoDetail" :subTitle="item.subTitle" :imgUrl="item.imgUrl" :title="item.title" v-for="(item,index) in serviceInfo" :key="index"></index-service>
       </div>
        <index-title :title="'新闻动态'" :subTitle="'News'"></index-title>
        <div class="more">查看更多</div>
        <div class="copyright">© 全友家私 蜀ICP备11013304号-2</div>
    </div>
  </scroll>

</template>

<script>
import scroll from '@/components/scroll'
import indexSlider from '@/components/index-slider'
import indexOrder from '@/components/index-order'
import indexHouseInfo from '@/components/index-house-info'
import sliderDots from '@/components/base/slider-dots'
import indexPanel from '@/components/index-panel'
import indexTitle from '@/components/base/index-title'
import indexService from  '@/components/base/index-service'
export default {
  data () {
    return {
      designerStatus:{
        isTransition: false,
        dots: [],
        loop: false,
        activeIndex: 0,
        dotBackgroundColor: false
      },

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
      house: {
        title: '全屋样板间',
        subTitle: 'WHOLE HOUSE MODEL ROOM',
        gallery: [
          {
            title: '欧美乡村空间 ',
            url: require('@/assets/images/home/country_style.jpg'),
          },
          {
            title: '美国田园空间 ',
            url: require('@/assets/images/home/america_field.jpg'),
          },
          {
            title: '现代简约空间',
            url: require('@/assets/images/home/modern_space.jpg'),
          },
          {
            title: '简约欧式空间 ',
            url: require('@/assets/images/home/simple_europe.jpg'),
          }
        ]
      },
      custom: {
        title: '定制风格',
        subTitle: 'CUSTOM STYLE',
        gallery: [
          {
            title: '新中式风格 ',
            url: require('@/assets/images/home/new_china.jpg'),
          },
          {
            title: '自然乡村风格 ',
            url: require('@/assets/images/home/nature_style.jpg'),
          },
          {
            title: '日式风格',
            url: require('@/assets/images/home/japan_style.jpg'),
          },
          {
            title: '现代轻奢风格 ',
            url: require('@/assets/images/home/modern_style.jpg'),
          },
          {
            title: '现代简约风格 ',
            url: require('@/assets/images/home/simple_style.jpg'),
          },
          {
            title: '现代轻奢风格 ',
            url: require('@/assets/images/home/popular_style.jpg'),
          },
        ]
      },
      wholeHouse: {
        title: '全屋定制',
        subTitle: 'WHOLE HOUSE CUSTOM',
        gallery: [
          {
            title: '简尚阳光 ',
            url: require('@/assets/images/home/sunshine.jpg'),
          },
          {
            title: '淳朴东方 ',
            url: require('@/assets/images/home/pure.png'),
          },
          {
            title: '西海岸印象',
            url: require('@/assets/images/home/west.png'),
          },
          {
            title: '友色空间 ',
            url: require('@/assets/images/home/friend.jpg'),
          },
          {
            title: '加州风情 ',
            url: require('@/assets/images/home/jiazhou.png'),
          },
          {
            title: '现代轻奢风格 ',
            url: require('@/assets/images/home/modern_space.jpg'),
          },
        ]
      },
      galleryList: [
        [
          require('@/assets/images/home/1.jpg'),
          require('@/assets/images/home/2.jpg')
        ],
        [
          require('@/assets/images/home/3.jpg'),
          require('@/assets/images/home/4.jpg')
        ],
        [
          require('@/assets/images/home/5.jpg'),
          require('@/assets/images/home/6.jpg')
        ],
        [
          require('@/assets/images/home/7.jpg'),
          require('@/assets/images/home/8.jpg')
        ],
        [
          require('@/assets/images/home/9.jpg'),
          require('@/assets/images/home/10.jpg')
        ]
      ],
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
      },
      serviceInfo: [
        {
          imgUrl:  require('@/assets/images/home/s0001.png'),
          subTitle:'幸福365服务',
          title: '售后保障',
          infoDetail: [
            '1. 3大阶段',
            '2. 6项服务',
            '3. 5项保障'
            ]
        },
        {
          imgUrl:  require('@/assets/images/home/s0002.png'),
          subTitle:'7x24小时快速响应',
          title: '在线报修',
          infoDetail: [
            '1. 便捷操作',
            '2. 及时响应'
            ] },
        {
          imgUrl:  require('@/assets/images/home/s0003.png'),
          subTitle:'全友就在你身边',
          title: '专卖店查询',
          infoDetail: [
            '1. 精准定位',
            '2. 一键查询'
            ]
        },
        {
          imgUrl:  require('@/assets/images/home/s0004.png'),
          subTitle:'服务飙升,体验升级',
          title: '售后保障',
          infoDetail: [
            '1. 免费在线预约',
            '2. 免费上门量尺',
            '3. 免费预算报价'
            ]
        },
      ]
    }
  },
  methods: {
    dotTopsStatus (info) {
      if (Array.isArray(info)) {
        [this.patch.dots, this.patch.activeIndex] = info
      }
    },
    dotsStatus (info) {
      console.log(info)
       if (Array.isArray(info)) {
        [this.designerStatus.dots, this.designerStatus.activeIndex] = info
      }
    }
  },
  components: {
    indexSlider,
    indexOrder,
    indexPanel,
    scroll,
    indexHouseInfo,
    sliderDots,
    indexTitle,
    indexService
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
    padding-bottom calc(39.73% + 30px)
    width 100%
    .name
      height 20px
      line-height 20px
      background #fff
      font-size 14px
      color #3e3e3e
      // overflow hidden
  .patch-bottom
    position relative
    height 60px
    width 100%
    background #f5f5f5
  .custom-style
    .custom-style-title
      display flex
      justify-content center
      align-items center
      height 66px
      width 100%
      background #eee
      text-align center
      .title
        font-size 20px
      .english-title
        margin-top 5px
        font-size 12px
        color #666 
  #designer
    width 100%
    display flex
    a
      width 50%
      box-sizing border-box
      padding 10px
 .designerStatus-patch-bottom
    position relative
    height 40px
    width 100%
  .service-container
    background #258566 
  .more
    width 80%
    height 40px
    line-height 40px
    text-align center
    border-radius 5px
    margin  20px 10% 20px 10%
    background  #3dc094  
    color #fff
  .copyright
    width 100%
    height 60px
    background #258566
    text-align center
    line-height 60px
    color #fff 
    // z-index -1
    // margin-bottom 100px  
</style>