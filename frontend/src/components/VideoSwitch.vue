<!-- <template>
    <div class="player">
        <Swiper :options="swiperOptions">
            <SwiperSlide>
                <div class="red"></div>
            </SwiperSlide>
            <SwiperSlide>
                <div class="blue"></div>
            </SwiperSlide>
            <SwiperSlide>
                <div class="green"></div>
            </SwiperSlide>
        </Swiper>
    </div>
</template>
<script >
import {Swiper ,SwiperSlide} from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/bundle';
export default{
    components:{
        Swiper,
        SwiperSlide,
    },
    data(){
        return {
      
     swiperOption: {
        direction:'vertical',
     }
    }

}
}
</script>

<style>

.red{
background-color: red;
margin: 0;
height: 500px;
width: 500px;
}
.blue{
background-color: blue;
margin: 0;
height: 500px;
width: 500px;
}
.green{
background-color: green;
margin: 0;
height: 500px;
width: 500px;
}
</style> -->





<template>
    <div class="area">
        <swiper
        :modules="modules"
        direction='vertical'
        navigation
        :pagination="{ clickable: true }"
        :scrollbar="{ draggable: true }"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        :loop="true"
        class="area"
        :options="swiperOptions"
        >
            <swiper-slide>
                    <video-player class="videocontent" :options="videoOptions"/>
            </swiper-slide>

            <swiper-slide>
                
                    <video-player class="videocontent" :options="videoOptions"/>
                
            </swiper-slide>

            <swiper-slide>
                
                    <video-player class="videocontent" :options="videoOptions"/>
                
            </swiper-slide>
           
        </swiper>
    </div>
  </template>
  <script>
    import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';
    // Import Swiper Vue.js components
    import { Swiper, SwiperSlide } from 'swiper/vue';
  
    // Import Swiper styles
    import 'swiper/css';
    import 'swiper/css/navigation';
    import 'swiper/css/pagination';
    import 'swiper/css/scrollbar';
  
    import VideoPlayer from '@/components/VideoPlayer.vue';

    export default {
      components: {
        Swiper,
        SwiperSlide,
        VideoPlayer,
      },
      data() {
    return {
        page:1,

      videoOptions: {
        autoplay: false,
        controls: true,
        // sources: [
        //   {
        //     src:
        //       'http://s360yyqhm.hn-bkt.clouddn.com/1.mp4',
        //       type: 'video/mp4',
        //   }
        // ]
      },

    //   swiperOptions: {
    //   // swiper组件提供的方法
    //   on: {
    //     tap: () => {
    //       // this.playAction(this.page - 1);
    //       console.log('点击: ', this.page);
    //     },
    //     slidePrevTransitionStart: () => {
    //       if (this.page > 1) {
    //         this.page -= 1;
    //       }
    //       // this.playAction(this.page - 1);
    //       console.log('下拉：', this.page);
    //     },
    //     slideNextTransitionStart: () => {
    //       this.page += 1;
    //       // this.playAction(this.page - 1);
    //       console.log('上滑：', this.page);
    //     },
    //   },
    // },
      
    };
  },
  setup() {
      const onSwiper = (swiper) => {
        console.log(swiper);
      };
      const onSlideChange = () => {
        console.log('slide change');
      };
      return {
        onSwiper,
        onSlideChange,
        modules: [Navigation, Pagination, Scrollbar, A11y],
      };
    },



    }
			
	
  </script>

  <style>
.area{
    height:800px;
    width:1250px;
    background:  rgb(22, 24, 35);;
}
.videocontent{
  margin:200px 100px;
}
.content-red{
    height: 600px;
    width: 600px;
    background-color: red;
}
.content-blue{
    height: 600px;
    width: 600px;
    background-color: blue;
}
.content-green{
    height: 600px;
    width: 600px;
    background-color: green;
}


</style>