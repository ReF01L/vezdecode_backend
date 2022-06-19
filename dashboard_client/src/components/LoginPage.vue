<template>
<div class="login">
    <input type="text" v-model="login">
    <input type="password" v-model="password">
    <div @click="auth">Авторизоваться</div>
    <div @click="sign_up">Зарегистрироваться</div>
    <div id="message">{{ message }}</div>
</div>
</template>

<script>
import axios from "axios";

export default {
    name: "LoginPage",
    data() {
        return {
            login: '',
            password: '',
            message: ''
        }
    },
    methods: {
        auth() {
            axios.post('http://127.0.0.1:8000/auth', {
                login: this.login,
                password: this.password
            })
            .then(res => {
                document.getElementById('message').innerText = res.data.message
            })
            .catch(err => {
                document.getElementById('message').innerText = err.response.message
            })
        },
        sign_up() {
            axios.post('http://127.0.0.1:8000/register', {
                login: this.login,
                password: this.password
            })
        }
    }
}
</script>

<style scoped>

</style>