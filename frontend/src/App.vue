<template>
    <router-view></router-view>
</template>

<script>


export default {
    name: 'App',
    components: {},
    data() {
        return {};
    },
    methods: {
        SendRequest() {
            axios.post('http://159.75.106.78:50000/api/auth/captcha', {
                username: '12345',
                password: 'qwer',
                email: '1252742605@qq.com',
                captcha: ''

            })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    }


};
</script>

<style>
button {
    width: 50px;
    height: 100px;
}

body {
    margin: 0;
}
</style>