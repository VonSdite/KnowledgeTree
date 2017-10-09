# 智慧树慕课视频自动观看

### 运行环境
- python 3.6.2
- python模块 selenium
- 谷歌浏览器， 谷歌浏览器的webdrvier

### 使用
```
from auto import AutoSeeVedio

if __name__ == '__main__':
    me = AutoSeeVedio(user='yourUserName', pwd='yourPassword')
    me.startAuto()
```

### 功能
- 实现自动登录智慧树
- 并且能自动继续学习并点掉智慧树的弹窗， 能挂机挂到看完视频
