#-- coding:UTF-8 --
import os
import platform
import shutil
import sys
import subprocess # python3.5以上自带

# 主窗
class App:
    def __init__(self):
        super().__init__()
        self.__path = os.path.split(os.path.realpath(__file__))[0]
        self.__handler = "protoc" # protoc脚手架
        self.__files = self.__path + "/protobuf/proto" # proto文件路径
        self.__compile = self.__path + "/protobuf/compile" # 编译后文件路径
        # 调起程序界面
        self.app_start()

    def app_start(self):
        self.protoc_handler()
        self.compile_proto()

    def protoc_handler(self): # 获取protoc脚手架
        info = subprocess.Popen("protoc --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        str = info.stdout.readline().decode("utf-8", "ignore")[0:9]
        if str != "libprotoc":
            system = platform.system()
            if system == "Win32": # windows32系统
                self.__handler = self.__path + "/protobuf/protoc-21.4-win32/bin/protoc"
            elif system == "Win64": # windows64系统
                self.__handler = self.__path + "/protobuf/protoc-21.4-win64/bin/protoc"
            elif system == "Darwin": # mac系统
                self.__handler = self.__path + "/protobuf/protoc-21.4-osx-x86_64/bin/protoc"

    def compile_proto(self): # 编译proto文件
        self.del_files()
        subprocess.Popen(self.__handler+" --php_out="+self.__compile+" --proto_path="+self.__files+" "+self.__files+"/*.proto", shell=True)
        print("编译成功，存放路径：" + self.__compile)

    def del_files(self): # 删除文件下所有内容
        for f in os.listdir(self.__compile):
            f_name = os.path.join(self.__compile, f)
            if os.path.isfile(f_name) == True: # os.path.isfile判断是否为文件
                os.remove(f_name)
            else:
                shutil.rmtree(f_name) # 删除文件夹及所有内容

    def get_proto_list(self, file_path = ""): # 获取所有proto文件
        files_arr = []
        if file_path == "":
            file_path = self.__files
        for f in os.listdir(file_path):  # listdir返回文件中所有目录
            f_name = os.path.join(file_path, f) # 当前文件夹的下面的所有东西的绝对路径
            if os.path.isfile(f_name) == True: # os.path.isfile判断是否为文件
                str = f[-6:]
                if str != ".proto":
                    continue
                files_arr.append(f_name)
            else:
                self.get_proto_list(f_name)

app = App()
