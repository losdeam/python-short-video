<template>
    <div id="background">
      <div id="contain">
        <h1>注册</h1>
        <div class="form">
          <label>用户名：</label>
          <input type="text" v-model.trim="name"><br/>
        </div>
        <div class="form">
          <label>密码：</label>
          <input type="password" v-model.trim="password"><br/>
        </div>
        <div class="form">
          <label>邮箱：</label>
          <input type="email" v-model.trim="mail"><br/>
        </div>
        <div class="form code-input">
          <label>验证码：</label>
          <input class="input_code" type="tel" v-model.trim="code"><br/>
          <button class="code_submit">获取验证码</button>
        </div>
        <button class="register_submit" @click.prevent="handlefinish">注册</button>
        
      </div>
    </div>
</template>
<style scoped>
#background{
  width: 100%;
    height: 100%;
    background: url("../assets/5.jpg");
    background-size:100% 100%;
    position: fixed;
    top: 0;
    left: 0;
}
#contain{
  width: 550px;
  height: 500px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background:#00000090;
  text-align: center;
  border-radius: 20px;
}
#contain h1{
  color: white;
}
.form{
  color: white;
  margin-left: 15%;
  margin-top: 60px;
  font-size: 20px;
  text-align: left;
}
label{
  float:left;
  width: 5em;
  margin-right: 1em;
  text-align: right;
}
input,textarea{
  margin-left: 10px;
  padding: 4px;
  border: solid 1px ;
  outline: 0;
  font: normal 13px/100% Verdana,Tahoma,sans-serif;
  width: 180px;
  height: 20px;
  background:#f1f1f190;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 8px;
  border-radius: 8px;
}
input:hover,textarea:hover,input:focus,textarea:focus{border-color:#0d0aa1;}
button{
  position: relative;
  height: 33px;
  width: 100px;
  background: rgba(148, 141, 235, 0.425);
  border-radius: 10px;
  margin-top: 38px;
  box-shadow: none;
  color: white;
  margin-left: 40px;
}
.code-input{
    display: flex;
}
.code_submit{
margin-top: 0px;
width: 100px;
height: 40px;
margin-left: 30px ;
}
.input_code{
    width: 100px;
}
.register_submit{
    margin-left: 0px;
    margin-top: 15px;
}
</style>
<script>
import { RouterLink } from 'vue-router';

export default {
    name: 'register',
    props: {
        msg: String
    },
    data() {
        return {
            name: "",
            password: "",
            mail: "",
            tel: ""
        };
    }, methods: {
        //点击完成按钮触发handlefinish
        handlefinish: function () {
            if (localStorage['name'] === this.name) {
                alert("用户名已存在"); //如果用户名已存在则无法注册
            }
            else if (this.name === '') {
                alert("用户名不能为空");
            }
            else { //将新用户信息存储到localStorage
                localStorage.setItem('name', this.name);
                localStorage.setItem('password', this.password);
                localStorage.setItem('mail', this.mail);
                localStorage.setItem('tel', this.tel);
                localStorage.setItem('s', "false");
                alert("注册成功");
                this.$router.replace('/Login'); //完成注册后跳转至登录页面
            }
        }
    },
    components: { RouterLink }
};
</script>