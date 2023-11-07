<template>
    <div>
      <video ref="videoPlayer" class="video-js" width="600"
      height="400">
      <source src="http://s360yyqhm.hn-bkt.clouddn.com/3.mp4?e=1699375411&token=JBmGTOlz7n8YQ4UQ3uqXvAEo9A9dMaw1eC1VOBKw:e5IK92nDL7AQbP68ohum5zB2pdY=" type="video/mp4" />
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




  