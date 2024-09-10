# Description
此为西南交通大学登陆wifi的脚本，有`python版本`和`shell版本`，可以把脚本放入路由器实现自动登录/共享网络的功能（一个宿舍只需要办一个网即可，打破常规mac限制

共享网络也可以路由器插wan在此网络环境下手动去登陆，登陆成功以后该路由整个nat环境都有网
# base theory
由于登陆并没有加入验证码防爬虫，所以理论上只需要知道手机号然后遍历1000-9999的验证码

本人办网络的时候没有告知我账号密码，于是只能采取这种方式。如果你知道账号密码，尽量使用账号密码减小路由负担

# usage

以下二选一

## init_campus_network.sh
修改脚本中的第49行手机号改为你的网络手机号
放入路由wan启动时运行即可

## login.py
修改第76行方法改为你的网络手机号参数，然后`python login.py`即可