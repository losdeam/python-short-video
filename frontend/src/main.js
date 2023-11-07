import { createApp } from 'vue'
import App from './App.vue'
// 导入路由
import router from '@/router'
// 导入http轻量库axios
import axios from 'axios'

// 配置axios默认域名
axios.defaults.baseURL = "http://127.0.0.1:5000"
// 前端cookie请求
axios.defaults.withCredentials = true
// 自定义vue属性http
Vue.prototype.$http = axios

const app = createApp(App)

app.use(router)

app.mount('#app')
