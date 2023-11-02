// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'


// import videojs from "video.js";
import "video.js/dist/video-js.css";
// Vue.prototype.$video = videojs;
import {Swipe, SwipeItem} from'vant'

app.use(Swipe).use(SwipeItem)
createApp(App).mount('#app')
