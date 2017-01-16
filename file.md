## 读写文件
### 文件与文件路径
import os
os.path.join('usr', 'bin', 'spam') => usr\binj\spam
当前工作目录：os.getcwd()
更改工作目录：os.chdir('C:\\Windows')
创建新文件夹：os.makedir(dir)
获取绝对路径：os.path.abspath(path)
判断路径：os.path.isabs(path)
路径间跳转计算：os.path.relpath(path, start) 从start到path的相对路径
基本名称：os.path.basename(path)
目录名称：os.path.dirname(path)
如：path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path) => 'calc.exe'
os.path.dirname(path) => 'C:\\Windows\\System32'
分离基本名称和目录名称：os.path.split(path)
os.path.split(path) => ('C:\\Windows\\System32', 'calc.exe')
os.path.sep = '\\'

文件字节数：os.path.getsize(path)
查看文件及文件夹：os.path.listdir(path)
检测路径是否存在：os.path.exists(path)
是否是文件：os.path.isfile(path）
是否是文件夹：os.path.isdir(path)
