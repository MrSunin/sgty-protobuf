SGTY服务器间通信协议
==================

# 使用protobuf

## protoc.py脚本

proto文件放在 protobuf/proto 下  
执行protoc.py脚本，会在 protobuf/compile 下生成编译好的脚本  
修改protoc.py中的compile_proto()方法中的"--php_out="换成对应编译的语言，例："--python_out="

## 电脑安装protoc编译器
[官方github](https://github.com/protocolbuffers/protobuf/releases)  
>protobuf下已经下载好了mac、win64、win32三个版本的编译器
>电脑可以不安装protoc编译器，protoc.py脚本会直接引用已经下载好的编译器

window下下载win32或者win64版本，mac下载osx版本，解压后得到可运行的脚本protoc
### Mac下安装：  
>把解压好的文件复制到 /usr/local 下对应的文件夹中
>完成后，通过 protoc --version 查看版本

~~~
cd protoc-21.4-osx-x86_64
cp -r include/ /usr/local/include/
cp -r bin/ /usr/local/bin/
~~~

### Windows下安装
>完成后，通过 protoc --version 查看版本  
>inlucde文件夹，下面有个google/protobuf ..里面都是使用proto的文件，不过不用管这里，直接用composer reuqire google/protobuf，会自动下载所需文件，并生成autoload.php 加载文件

把解压好的protoc-21.4-win64拷贝到D盘 D:\protoc-21.4-win64  
添加到环境变量中，我的电脑 -> 右键属性 -> 高级 -> 环境变量 ->  
用户变量添加， Path: D:\protoc-21.4-win64\bin
系统变量添加，PROTOBUF_HOME : D:\protoc-21.4-win64\bin

## 使用python执行shell命令，编译proto
编写的python文件：extend/protoc.py
使用subprocess执行shell命令行
~~~
......
import subprocess
......
subprocess.Popen("protoc --php_out=protobuf/compile --proto_path=protobuf/proto protobuf/proto/*.proto", shell=True)
# 第一个路径为 生成文件的位置，第二个为存储proto文件的位置，第三个表示当前文件下所有proto文件
# proto文件需要在同一目录下，不能在子文件夹下
~~~

## 安装composer依赖扩展
>当前项目下安装依赖扩展
~~~
composer require google/protobuf
# 国内镜像可能下载失败，可以将镜像改为 https://repo.packagist.org
~~~
