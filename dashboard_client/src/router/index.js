import {createWebHistory, createRouter} from "vue-router"
import DashboardPage from "@/components/DashboardPage";
import ImagePage from "@/components/ImagePage";
import LoginPage from "@/components/LoginPage";


const routes = [
    {
        path: "/",
        name: DashboardPage.name,
        component: DashboardPage,
    },
    {
        path: "/images",
        name: ImagePage.name,
        component: ImagePage
    },
    {
        path: "/login",
        name: LoginPage.name,
        component: LoginPage
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router