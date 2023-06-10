import {createRouter, createWebHashHistory} from 'vue-router'
import HomeView from "@/views/HomePageView";
import TipsView from "@/views/TipsHelpView";


const routes = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        name: 'HomePageView',
        component: HomeView
    },
    {
        path: '/recomendations',
        name: 'TipsHelpView',
        component: TipsView
    }
]



const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
