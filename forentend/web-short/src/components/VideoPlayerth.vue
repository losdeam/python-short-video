<template>
    <div>
      <video ref="videoPlayer" class="video-js" width="600"
      height="400">
      <source src="http://s360yyqhm.hn-bkt.clouddn.com/%E5%9F%83%E5%8F%8A%E5%A5%B3%E5%AD%90%E6%80%92%E6%96%A5%E7%BE%8E%E5%9B%BDCNN%E8%AE%B0%E8%80%85%E4%BD%A0%E4%BB%AC%E5%B0%B1%E6%98%AF%E6%B2%A1%E6%9C%89%E4%BA%BA%E6%80%A7%E7%9A%84%E4%BC%A0%E5%A3%B0%E7%AD%92%E5%82%80%E5%84%A1.mp4?e=1699372432&token=JBmGTOlz7n8YQ4UQ3uqXvAEo9A9dMaw1eC1VOBKw:1Kj07z6OEAFK6fX3kFr6xTIdYv4=" type="video/mp4" />
    </video>
      <!-- <video ref="videoPlayer" class="video-js">
        <source src="/src/assets/naitang.mp4" type="video/mp4" />
      </video> -->
      <!-- <button @click="click_switch"></button> -->
    </div>
  </template>
  
  <script>
  
import videojs from 'video.js';
import axios from 'axios';  
  export default {

    name: 'VideoPlayer',
    props: {
      options: {
        type: Object,
        default() {
          return {};
        }
      }
    },
    data() {
      return {
        player: null,
        videourl: "",
      }
    },
    created() {
      this.getvideo();
    },
    mounted() {
      
      this.player = videojs(this.$refs.videoPlayer, this.options, () => {
        this.player.log('onPlayerReady', this);
      });
      this.player.on('error', (error) => {
      console.error('Video.js error:', error);
      });
    },
    beforeDestroy() {
      if (this.player) {
        this.player.dispose();
      }
    },

    methods:{
      getvideo() {
        axios.get("http://159.75.106.78:50000/api/video/sortvideos/" + '3')
        .then((res) => {
          this.videourl = res.data.url_video;
          console.log(this.videourl);

                });},

      click_switch(){
        console.log(2)
      },
    }
  };
  
  </script>

<style scoped>
.video-js{
  width: 800px;
  height: 500px;
  border-radius: 3%;
  
}
button{
  height: 50px;
  width: 100px;
}
</style>




  