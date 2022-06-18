import { createApp } from 'vue'
import axios from "axios";
import VueAxios from "vue-axios";
import App from './App.vue'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

createApp(App).use(VueAxios, axios).mount('#app')