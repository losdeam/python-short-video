<template>
    <div>
        <div class="window-body">
            <div class="body-left">
                <div class="body-left_head">
                    <RouterLink to="/layout"><img class="T-Logo" src="../assets/Icons/T-LOGO.svg"></RouterLink>
                    <div class="T-Text">光子短视频</div>
                </div>
                <div class="body-left_bar">
                    <div class="leftbar-items">
                        <img class="leftbar-items_icons" src="../assets/Icons/whitejian.svg">
                        <div class="leftbar-items_text front">推 荐</div>
                    </div>
                    <div class="leftbar-items">
                        <img class="leftbar-items_icons" src="../assets/Icons/hot.svg">
                        <div class="leftbar-items_text ">热 点</div>
                    </div>
                    <div class="leftbar-items">
                        <img class="leftbar-items_icons" src="../assets/Icons/tiyu.svg">
                        <div class="leftbar-items_text ">体 育</div>
                    </div>
                    <div class="leftbar-items">
                        <img class="leftbar-items_icons" src="../assets/Icons/dongman.svg">
                        <div class="leftbar-items_text ">动 漫</div>
                    </div>
                    <div class="leftbar-items">
                        <img class="leftbar-items_icons" src="../assets/Icons/youxi.svg">
                        <div class="leftbar-items_text ">游 戏</div>
                    </div>
                    <div class="leftbar-items">
                        <img class="leftbar-items_icons" src="../assets/Icons/keji.svg">
                        <div class="leftbar-items_text">科 技</div>
                    </div>
                </div>
            </div>
            <div class="body-right">
                <div class="body-right_head">
                    <div></div>
                    <div class="signin">
                        <div class="rightbar-items">
                            <img class="rightbar-items_icons" src="../assets/Icons/tongzhi.svg">
                            <div class="rightbar-items_text">通知</div>
                        </div>
                        <div class="rightbar-items">
                            <img class="rightbar-items_icons" src="../assets/Icons/lishi.svg">
                            <div class="rightbar-items_text">历史</div>
                        </div>
                        <div class="rightbar-items">
                            <img class="rightbar-items_icons" src="../assets/Icons/shoucang.svg">
                            <div class="rightbar-items_text">收藏</div>
                        </div>
                        <div class="rightbar-items">
                            <div class="touxiang">头像</div>
                        </div>
                    </div>
                </div>
                <div class="body-right_playerarea">
                    <div class="videoarea">
                            <video-switch class="video_switch"></video-switch>
                    </div>
                    <div class="switchbutton"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import VideoPlayer from '@/components/VideoPlayer.vue';
import Like from '@/components/Like.vue'
import VideoSwitch from '@/components/VideoSwitch.vue';
import { RouterLink } from 'vue-router';
export default {
  name: 'VideoExample',
  components: {
    VideoPlayer,
    VideoSwitch,
    Like,
    RouterLink
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
methods:{
    Click(){
        console.log(1)
        
    }
    
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
    height: 100%;
    width: 100%;
    
}
.window-body .body-left{
    height: 100%;
    background:  rgb(22, 24, 35);
    flex-shrink: 0;
    position: relative;
    --container-background: linear-gradient(180deg,#060716 80%,#06071600);
    /* background-image: linear-gradient(109.6deg, rgb(0, 51, 102) 11.2%, rgb(187, 187, 187) 91.1%); */
}

.body-left_head{
    display: flex;
    height: 68px;
    position: relative;
    background-color:rgb(238, 234, 234);
}

.T-Logo{
    width: 54px;
    height: 60px;
}
.T-Text{
    text-align: center;
    margin-top: 20px;
    margin-right: 10px;
    margin-left: 5px;
    font-family: "Alimamashu";
    font-size: 24px;
}
.leftbar-items{
    display:flex;
}
.leftbar-items_icons{
    width: 25px;
    height: 25px;
    margin-top: 30px;
    margin-left: 30px;
    margin-right: 20px;
    
}
.leftbar-items_text{
    color: whitesmoke;
    margin: 30px;
    margin-left: 0;
    font-family: "Alimamayuan";
    font-size: 20px;
}
.front{
    margin-bottom: 100px;
}
.body-right{
    background-color:  rgb(22, 24, 35);
    width: 100%;

}
.signin{
   display: flex;
   background-color:rgb(238, 234, 234);

}
.rightbar-items{
    margin: 20px;
}
.touxiang {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    color: #fff;
    background: #00AEEC;
    text-align: center;
    letter-spacing: 0;
    font-size: 14px;
    line-height: 36px;
}
.rightbar-items_icons{
    width: 25px;
    height: 25px;
    margin-left: 3px;
}
.rightbar-items_text{
    font-family: "Alimamayuan";
    font-weight: 550;
}
.body-right_head{
    display: flex;
    height: 68px;
    background-color:rgb(238, 234, 234);
    justify-content: space-between;
    flex: 1;
}
.body-right_playerarea{
    display: flex;
    width: 1300px;
    flex: 1;
}

.switchbutton{
    width: 50px;
    background-color:  rgb(22, 24, 35);
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


button{
    height: 100px;
    width: 100px;
}      
body{
    margin: 0;
    padding: 0;
}

</style>