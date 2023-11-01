
<template>
  <!-- <div class="windows"> -->
    <layout></layout>
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

export default {
  components: {
    Layout,
  },
  data() {
    return {
    
    };
  }


};

import axios from 'axios'

// 向给定ID的用户发起请求
axios.get('http://159.75.106.78:50000/test_1')
  .then(function (response) {
    // 处理成功情况
    console.log(response);
  })
  .catch(function (error) {
    // 处理错误情况
    console.log(error);
  })
  .finally(function () {
    // 总是会执行
  });
</script>

<style>

body{
  margin: 0;
}

</style>