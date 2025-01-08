# 文件随机

## 需求

有文件夹结构如下：

```dirs
- videos
  - video1.mp4
  - video2.mp4
  - ...
  - videoN.mp4
- texts
  - text1.txt
  - text2.txt
  - ...
  - textN.txt
```

请开发一个 Python GUI 程序，帮我实现如下功能：

- 输入参数
  - 视频目录路径（文件选择组件）
  - 文本文件目录路径（文件选择组件）
  - 视频文件数量，区间形式，eg: 4-6
  - 文本文件数量，区间形式，eg: 1-1
  - 生成文件数量
  - 生成文件保存路径
- 可以记住上次输入参数
- 根据用户输入，从“视频目录路径”中随机选取“视频文件数量”个视频文件，
- 从“文本文件目录路径”中随即选取“文本文件数量”个文本文件，
- 在“生成文件保存路径”中生成一个自然数字命名的目录，
- 将前面随机选取的视频文件和文本文件复制到该目录中；
- 重复上述步骤，直到生成“生成文件数量”个目录。

## 打包

```bash
# pip install pyinstaller

pyinstaller --name "VTRC" --onefile --windowed --icon=icon.ico --upx-dir=upx --clean main.py

# macOS
pyinstaller --name "VTRC" --onefile --windowed --icon=icon.icns --upx-dir=upx --clean main.py

# Linux
pyinstaller --name "VTRC" --onefile --windowed --icon=icon.png --upx-dir=upx --clean main.py
```
