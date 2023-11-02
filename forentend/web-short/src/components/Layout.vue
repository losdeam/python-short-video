<template>
    <div>
        <div class="window-body">
            <div class="body-left">
                <div class="body-left_head">
                    <img src="../assets/xiazai.png">
                </div>
                <div class="body-left_bar">
                    <div class="leftbar-items front">推 荐</div>
                    <div class="leftbar-items">热 点</div>
                    <div class="leftbar-items">体 育</div>
                    <div class="leftbar-items">娱 乐</div>
                    <div class="leftbar-items">游 戏</div>
                    <div class="leftbar-items">科 技</div>
                </div>
            </div>
            <div class="body-right">
                <div class="body-right_head">
                    <div>111111111111111111111</div>
                    <div class="signin">
                        <div class="rightbar-items">1</div>
                        <div class="rightbar-items">2</div>
                        <div class="rightbar-items">3</div>
                    </div>
                </div>
                <div class="body-right_playerarea">
                    <div class="videoarea">
                        <div class="video-content">
                            <!-- <video-player :options="videoOptions"/>  -->
                            <switchvideo></switchvideo>

                        </div>
                    </div>
                </div>
                <div class="switchbutton"></div>
            </div>
        </div>
    </div>
</template>
<script>
import VideoPlayer from '@/components/VideoPlayer.vue';
import switchvideo from './switchvideo.vue';
export default {
  name: 'VideoExample',
  components: {
    VideoPlayer,
    switchvideo,
  },
  data() {
    return {
      videoOptions: {
        autoplay: false,
        controls: true,
        sources: [
          {
            src:
              'http://s360yyqhm.hn-bkt.clouddn.com/1.mp4',
              type: 'video/mp4',
          }
        ]
      }
    };
  }
};
</script>
<style scoped>
.window-body{
    background-color: rgb(22, 24, 35);
    background-position: top;
    background-size: cover;
    display: flex;
    flex: 1;
    flex-direction: row;
    height: 100vh;
    width: 100%;
    
}
.window-body .body-left{
    height: 100%;
    background:  rgb(22, 24, 35);
    flex-shrink: 0;
    position: relative;
    --container-background: linear-gradient(180deg,#060716 80%,#06071600);
}

.body-left_head{
    height: 68px;
    position: relative;
    background-color: bisque;
}
.leftbar-items{
    color: whitesmoke;
    margin: 30px;
    margin-left: 50px;
}
.front{
    margin-bottom: 100px;
}
.body-right{
background-color: blue;
width: 100%;

}
.signin{
   display: flex;
   background-color: blueviolet;

}
.rightbar-items{
    margin: 20px;
}
.body-right_head{
    display: flex;
    height: 68px;
    background-color: aqua;
    justify-content: space-between;
    flex: 1;
}
.videoarea{
  text-align: center;
  position: relative;
}
.video-content {
      display: flex;
      justify-content: center;
      flex-direction: column;
      align-items: center;
      margin: 20px;
      }
body{
    margin: 0;
    padding: 0;
}

</style>