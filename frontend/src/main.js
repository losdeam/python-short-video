// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from'../src/components/router'
import "video.js/dist/video-js.css"
import "./assets/font/font.css"

const app = createApp(App)

app.use(router)

app.mount('#app')
