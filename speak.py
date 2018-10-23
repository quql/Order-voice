from playsound import playsound
import redis
import time

pool = redis.ConnectionPool(host='192.168.81.69', port=6379)

r = redis.Redis(connection_pool=pool)
print('*****订单监听系统********')
print('************************')
print('**开始监听新的订单中*****')
print('************************')


while True:
    name = r.lpop('yuyinlist')
    if name == None:
        time.sleep(3)
    else:
        playsound("audio.mp3")
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print('speak..'+now)



# print(name.decode('utf-8'))