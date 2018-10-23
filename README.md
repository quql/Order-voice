# Python和Redis实现订单监听,语音播报

1.MP3格式的音频文件 如 audio.mp3

2.创建虚礼环境

创建虚拟环境
安装：pip install virtualenv
创建：virtualenv venv
激活：venv\Scripts\activate

3.安装所需扩展

pip install playsound 

pip install redis

3.编写python代码

4.解决问题：python写的小脚本需要在几千台电脑上运行，省去运维人员安装python的麻烦，直接exe程序运行。

工具：pyinstaller

下载及安装：pip install pyinstaller

然后就等待吧，这个命令先下载pyinstaller,然后又自动安装，等到100%搞定后。



执行命令：pyinstaller -F speak.py
--------------------- 
5.将音频文件和打包生成的speak.exe放在同一个文件夹即可使用

## 原理:

python监听 redis队列,有值播放音频文件

