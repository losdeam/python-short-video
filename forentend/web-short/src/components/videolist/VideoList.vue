
<!-- <template>
  <div class="hello">
    <div v-for="(item,i) in list" :key="i" style="margin-bottom: 30px">
      <video :id="'myVideo'+item.id" class="video-js">
        <source :src="item.src" type="video/mp4">
      </video>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
    data(){
      return {
          list:[
              {
                  src:'http://img.yopoo.cn/banner_video.mp4 ',
                  id:0,
                  pic:"",
              },
              {
                  src:'http://img.yopoo.cn/banner_video.mp4 ',
                  id:1,
                  pic:"",
              },
              {
                  src:'http://img.yopoo.cn/banner_video.mp4 ',
                  id:2,
                  pic:"",
              }
          ]
      }
    },
    mounted() {
        this.initVideo();
    },
    methods: {
        initVideo() {
            //初始化视频方法 循环列表获取每个视频的id
            this.list.map((item,i)=>{
                let myPlayer = this.$video('myVideo'+item.id, {
                    //确定播放器是否具有用户可以与之交互的控件。没有控件，启动视频播放的唯一方法是使用autoplay属性或通过Player API。
                    controls: true,
                    //自动播放属性,muted:静音播放
                    autoplay: "muted",
                    //建议浏览器是否应在<video>加载元素后立即开始下载视频数据。
                    preload: "auto",
                    //设置视频播放器的显示宽度（以像素为单位）
                    width: "800px",
                    //设置视频播放器的显示高度（以像素为单位）
                    height: "400px",
                    //封面图
                    poster:item.pic
                });
            })

        }
    }
}
</script>
