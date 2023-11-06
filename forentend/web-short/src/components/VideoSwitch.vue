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
        >
            <swiper-slide>
                <div class="content-red">
                    <video-player :options="videoOptions"/>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="content-blue">
                    <div></div>
                    <video-player :options="videoOptions"/>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="content-green">
                    <div></div>
                    <video-player :options="videoOptions"/>
                </div>
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
      }
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
    };
  </script>

  <style>
.area{
    height: 600px;
    width: 600px;
    background-color: bisque;
}
.content-red{
    height: 400px;
    width: 400px;
    background-color: red;
}
.content-blue{
    height: 400px;
    width: 400px;
    background-color: blue;
}
.content-green{
    height: 400px;
    width: 400px;
    background-color: green;
}


</style>