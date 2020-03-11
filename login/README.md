基础包：selenium,pyautogui

淘宝登陆反爬虫策略：
1.selenium反爬
正常浏览器(console)：
>window.navigator.webdriver
>undefined
使用selenium:
>window.navigator.webdriver
>true
解决：
>Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});

2.滑动验证码
先输入用户名==>接着输入密码==>会出现滑动验证码
解决：
先输入密码==>接着输入用户名==>不会出现验证码

小结：在打开网页，通过了步骤1后，JavaScript脚本会继续监听selenium的点击和输入事件直到登陆成功。
