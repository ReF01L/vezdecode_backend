<template>
    <div class="image">
        <div class="image-title">{{ current_image['photo_id'] }}</div>
        <img :src="`http://127.0.0.1:8000${current_image.image}`" alt="" class="image-image">
        <div class="image_btns">
            <div class="image_btns-like" @click="like">Лайк</div>
            <div class="image_btns-likes">Лайков: {{ current_image['likes'] }}</div>
            <div class="image_btns-skip" @click="next">Скип</div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "ImagePage",
    data() {
        return {
            image: {},
            images: [],
            remaining: 0,
            total: 0
        }
    },
    methods: {
        next() {
            this.remaining -= 1
            if (this.remaining === 0) {
                this.remaining = this.total
            }

            axios.get(`http://127.0.0.1:8000/posts/${this.images[this.total - this.remaining]['id']}`)
                .then(res => {
                    this.image = res.data
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        like() {
            axios.get('http://127.0.0.1:8000/post/like', {
                params: {
                    photo_id: this.image['photo_id'],
                    user_id: 1
                }
            })
                .then(() => {
                    this.next()
                })
                .catch(err => {
                    console.log(err.response)
                })
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/posts')
            .then(res => {
                this.images = res.data['photos']
                this.remaining = res.data['count']
                this.total = res.data['count']

                axios.get(`http://127.0.0.1:8000/posts/${this.images[0]['id']}`)
                    .then(res => {
                        this.image = res.data
                    })
                    .catch(err => {
                        console.log(err.response)
                    })

            })
            .catch(err => {
                console.log(err.response)
            })
    },
    computed: {
        current_image() {
            return this.image
        }
    }
}
</script>

<style scoped>
.image {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.image-title {
    font-size: 22px;
    margin-bottom: 15px;
}

.image-image {
    max-width: 420px;
    min-width: 100px;
    min-height: 100px;
    max-height: 320px;
    display: block;
    margin-bottom: 25px;
    margin-top: 10px;
}

.image_btns {
    display: flex;
    justify-content: space-between;
    width: 320px;
}

.image_btns-like {
    border: 1px solid black;
    padding: 5px;
}

.image_btns-likes {
    border: 1px solid black;
    padding: 5px;
}

.image_btns-skip {
    border: 1px solid black;
    padding: 5px;
}
</style>