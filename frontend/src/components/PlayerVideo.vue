<!-- controls：向用户显示播放按钮控件 -->
<template>
    <video
      ref="video"
      class="video-js vjs-default-skin"
      width="600"
      height="400"
      controls
    >
      <source src="https://playtv-live.ifeng.com/live/06OLEGEGM4G.m3u8" />
    </video>
  </template>
  <script>
  export default {
    data() {
      return {
        player: null, // 用来存储当前 video
      };
    },
    mounted() { // 渲染视频
      this.player = this.$video(this.$refs.video);
    },
  };
</script>
