import { createApp } from 'vue'
import axios from "axios";
import VueAxios from "vue-axios";
import App from './App.vue'
import router from "@/router";

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

createApp(App).use(router).use(VueAxios, axios).mount('#app')