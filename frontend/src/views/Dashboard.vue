<template>
    <div class="homeWrap">
        <el-container style="height: 100%; border: 1px solid #eee">
            <el-container>
                <el-main>

                    <!--声明路由占位符标签-->
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>



<script>
export default {
    components: {},
    name: "Dashboard",
    data() {
        return {
            name: "王小晖",
        };
    },
    created: function () {
        // this.$http.get("profile/show").then((res) => {
        //     this.name = res.data[0].name;
        // });
    },
    methods: {
        logout() {
            this.$http
                .get("/logout")
                .then((res) => {
                    if (res.data.code === 1) {
                        this.$message.success("退出登录成功");
                        this.$router.push("/login");
                    }
                })
                .catch((err) => {
                    this.$message.warning("退出登录失败");
                    console.log(err);
                });
        },
    },
};
</script>


<style>
.el-header {
    background-color: #edf5fd;
    color: rgb(31, 36, 41);
    line-height: 60px;
}

.el-aside {
    color: #333;
    box-shadow: 2px 0 6px rgb(125, 133, 141);
}

/* 去除滚动条 */
.el-aside::-webkit-scrollbar {
    display: none;
}

.homeWrap {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
