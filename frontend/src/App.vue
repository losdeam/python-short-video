
<template>
  <!-- <div class="windows"> -->

    <!-- <layout></layout> -->
    <!-- <VideoSwitch></VideoSwitch> -->
    <!-- <signin></signin> -->
    <RouterLink to="/layout"><button></button></RouterLink>
    <RouterLink to="/videoswitch"><button></button></RouterLink>
    <RouterView></RouterView>
    <!-- <button @click="SendRequest"></button> -->
    <!-- <div class="videoarea">
      <div class="video-content">
        <video-player :options="videoOptions"/>
      </div>
    </div> -->
  <!-- </div> -->

</template>

<script>
import VideoPlayer from '@/components/VideoPlayer.vue';
import Layout from './components/Layout.vue';
import VideoSwitch from './components/VideoSwitch.vue';
import Signin from './components/Signin.vue';
import Register from './components/Register.vue';
import axios from 'axios'
import { RouterView } from 'vue-router';
export default {
  components: {
    Layout,
    VideoSwitch,
    Signin,
    Register,
    RouterView
},
  data() {
    return {
    
    };
  },
  methods:{
    SendRequest(){
      axios.post('http://159.75.106.78:50000/api/auth/captcha', {
    username: '12345',
    password: 'qwer',
    email:'1252742605@qq.com',
    captcha:''

  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
  }
    }
  

};

// import axios from 'axios'

// // 向给定ID的用户发起请求
// axios.get('http://159.75.106.78:50000/test_1')
//   .then(function (response) {
//     // 处理成功情况
//     console.log(response);
//   })
//   .catch(function (error) {
//     // 处理错误情况
//     console.log(error);
//   })
//   .finally(function () {
//     // 总是会执行
//   });

// axios.post('http://159.75.106.78:50000/api/auth/captcha', {
//     username: '12345',
//     password: 'qwer',
//     email:'1252742605@qq.com',

//   })
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     console.log(error);
//   });
</script>

<style>

button{
  width: 50px;
  height: 100px;
}
body{
  margin: 0;
}

</style>