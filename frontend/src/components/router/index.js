import { createRouter,createWebHistory } from 'vue-router';
import Layout from '@/components/Layout.vue';
import VideoSwitch from '@/components/VideoSwitch.vue';


const router =createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            component:Layout,
        },
        {
        path:'/layout',
        component:Layout,
        name:"Layout"
        },
        
        {
        path:'/videoswitch',
        component:VideoSwitch
        },
        
            ]
})

export default router
