<template>
    <div>
      <video ref="videoPlayer" class="video-js" width="600"
      height="400">
      <source src="http://s360yyqhm.hn-bkt.clouddn.com/1.mp4" type="video/mp4" />
    </video>
      <!-- <video ref="videoPlayer" class="video-js">
        <source src="/src/assets/naitang.mp4" type="video/mp4" />
      </video> -->
      <!-- <button @click="click_switch"></button> -->
    </div>
  </template>
  
  <script>
  
import videojs from 'video.js';
  
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
        player: null
      }
    },
    mounted() {
      this.player = videojs(this.$refs.videoPlayer, this.options, () => {
        this.player.log('onPlayerReady', this);
      });
    },
    beforeDestroy() {
      if (this.player) {
        this.player.dispose();
      }
    },

    methods:{
      click_switch(){
        console.log(2)
        
      }
    },
  }
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




  