# 一、项目介绍
该项目为七牛云 2023 年 1024 创作节校园编程马拉松参赛作品
本项目采用python语言开发一个短视频平台，使用flask作为后端架构，作为系统整体架构，采用mysql和redis做数据的持久化操作。
# 二、项目分工
[losdeam](https://github.com/losdeam)：视频管理模块设计，推荐系统设计，框架分析与设计
[Chunfield](https://github.com/Chunfield)：前端
[komiblog](https://github.com/komiblog)：用户模块设计，数据库，框架优化
# 三、项目实现
### 3.1 相关开发文档
[视频管理模块设计](doc/视频管理模块设计.md)
[用户模块设计](doc/用户模块设计.md)
[播放模块设计](doc/播放模块设计.md)

### 3.2 架构设计


![](https://cdn.nlark.com/yuque/0/2023/jpeg/40362764/1699356375136-b2585e6a-fc10-44a4-b05a-16bb76851110.jpeg)
#### 
### 3.3 项目代码运行介绍
#### 前端部分：
环境需求：
  vue3
 	nodejs16
运行代码：
```bash
npm instll
```
```bash
npm run dev
```
```bash
npm run build
```

#### 后端代码：
环境需求：
python 3.10
运行代码;
```bash
pip install -r requirements.txt instll
```

#### 数据库：
环境需求：
mysql
redis
Docker-Compose
运行代码;
```bash
docker composee up -d
```


# 四、Demo 演示视频 
基础功能_视频地址：s360yyqhm.hn-bkt.clouddn.com/比赛视频_1.mp4
强化功能_视频地址：s360yyqhm.hn-bkt.clouddn.com/比赛视频_2.mp4
# 五、项目总结与反思

1. 目前仍存在的问题

2. 已识别出的优化项
   1.  推荐系统的冷启动后续可优化为根据用户当前所给的信息判断大致偏好
   2.  推荐系统可创建针对于指定人群的模型，再对指定人群进行推荐时可额外调用该模型来优化推荐结果

3. 项目过程中的反思与总结


