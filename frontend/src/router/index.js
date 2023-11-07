import { createRouter, createWebHistory } from 'vue-router';

import Layout from '@/components/Layout.vue';
import VideoSwitch from '@/components/VideoSwitch.vue';
// 导入组件
import Dashboard from '@/views/Dashboard.vue';


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Dashboard, },
        // { path: '/layout', component: Layout, name: "Layout" },
        // { path: '/videoswitch', component: VideoSwitch },
    ]
})

export default router
