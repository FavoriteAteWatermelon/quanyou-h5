# 全有家私H5
## 主目录文件
nuxt.js为express与vue的结合体
server:端的主入口在server/index.js
client:主入口在.nuxt/index.js

### 动画方面
同时转动和移动位子的动画:用绝对定位+transform,单纯的transform没法完成
### vue-awesome-swiper体验优化 css加载本地图片 template加载本地图片
1. 使用默认图片padding-bottom的方式加载，不会有图片占位子的存在

2. css加载图片的方式为background url('~@/assets/images/common/default.png') center no-repeat

3. template引入背景图片的方式是 :style="{backgroundImage:'url('+require('@/assets/images/home/swiper1.jpg')+')'}"

