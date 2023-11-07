import { createRouter,createWebHistory } from 'vue-router';
import Layout from '@/components/Layout.vue';
import VideoSwitch from '@/components/VideoSwitch.vue';
import Signin from '@/components/Signin.vue';
import Register from '@/components/Register.vue';


const router =createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            component:Signin,
        },
        {
        path:'/layout',
        component:Layout,
        name:"Layout"
        },

        {
        path:'/register',
        component:Register,
        name:"Register"
        },
        {
        path:'/signin',
        component:Signin,
        name:"Signin"
        },
        
        {
        path:'/videoswitch',
        component:VideoSwitch
        },
        
            ]
})

export default router
