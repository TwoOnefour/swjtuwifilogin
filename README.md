# Description
此为西南交通大学登陆wifi的脚本，有`python版本`和`shell版本`，可以把脚本放入路由器实现自动登录/共享网络的功能（一个宿舍只需要办一个网即可，打破常规mac限制

**做了教学区登陆逻辑是因为这个网一段时间后就会自动掉线,明明是有网络流量的,很不合理,每次断网就想骂人**

**请自行判断你的供应商是电信还是教育网，电信请使用dormitory下的脚本**
共享网络也可以路由器插wan在此网络环境下手动去登陆，登陆成功以后该路由整个nat环境都有网
# base theory
由于登陆并没有加入验证码防爬虫，所以理论上只需要知道手机号然后遍历1000-9999的验证码

本人办网络的时候没有告知我账号密码，于是只能采取这种方式。如果你知道账号密码，尽量使用账号密码减小路由负担

# usage
有宿舍区和教学区的脚本, 请自行查看 `login.py` 或 `Dormitory/login.py`
以下二选一

## init_campus_network.sh
**此脚本已废弃，目前需要加密，用python比较方便，有兴趣的也可以用openssl库实现**
~~修改脚本中的第49行手机号改为你的网络手机号~~
~~放入路由wan启动时运行即可~~

## login.py
修改第76行方法改为你的网络手机号参数，然后`python login.py`即可

# update
记录一下我和学校网管相爱相杀的日志

## 2024/09/25 更新，传递参数的方式变为加密，已实现

## 2024/10/16 添加了mac屏蔽，路由器中改wan口mac即可绕过

## 2024/10/17 新增了登陆页面，登陆后的用户可以看到自己的mac和登陆的设备，以前不管是否登录都是跳转到账号密码登陆页面。网络中心还是会干正事的

## 2024/11/02 之前把设备名称默认名称改为了`下次换RSA加密吧，AES太简单了`。在我的热心建议下，网管把加密改成了`RSA+AES`加密

javascript代码里甚至还有`sb250`的`list`，差点没笑死

![AES加密数组里有SB250](https://bucket-cf.voidval.com/github_img/20241105-145153.png)

随便写一下就实现了，挺简单的，拿到`public_key`以后`RSA加密`数据，之后再拿到AES的`key`和`iv`，再加密一次就行了

![设备名](https://bucket-cf.voidval.com/github_img/3a952116d142257fcb5a0f625a843072.png)

## 2024/11/07 更新了js混淆，网络中心真狠啊，还没实现，等我逆向一下

晚上八点 把RSA的key和iv写对了以后，后端从认证异常变成了你猜对不对，我蹦不住了

加密算法不正确的时候提示的是认证异常
![加密算法不正确的时候提示认证异常](https://bucket-cf.voidval.com/github_img/df7c51b9d89fc921105bc9f7ef3d14b7d3c81969.png)

![加密算法正确了以后](https://bucket-cf.voidval.com/github_img/7558056557728d33cd172084149d9eb396195fee.png)


23:28 这个你猜对不对的提示是对json请求做了校验，没有对应的参数就不能通过
勉强在熄灯前打上断点把参数逆向出来了，这次确实挺有难度的
![拿下](https://bucket-cf.voidval.com/github_img/3C468D00C543795E03853A65FDD68D25.png)


## 2025/03/14

更新教学区登入逻辑，根本不需要怎么动脑
![](https://bucket.voidval.com/upload/2025/03/dc26d6b797daf27fefdb9f1e0bd379b4.png)


## 2025/03/17

网络中心是不是没活了，把我的域名dns污染了
![](https://bucket.voidval.com/upload/2025/03/1709661bfd304a2fa537b778bd57f797.png)

那我走个tls查询dns你又该如何应对？

![](https://bucket.voidval.com/upload/2025/03/6054dcf0bb77650e8440f3cfa7af6e1c.png)

![](https://bucket.voidval.com/upload/2025/03/cdf0e2fee462e14a996e58797b842d57.png)

