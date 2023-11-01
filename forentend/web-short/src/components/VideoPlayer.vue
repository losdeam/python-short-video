<template>
    <div>
      <video ref="videoPlayer" class="video-js" width="600"
      height="400"></video>
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
    }
  }
  </script>

<style scoped>
.video-js{
  width: 1000px;
  height: 550px;
  
}
</style>
  