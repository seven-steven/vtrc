from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                           QLabel, QLineEdit, QPushButton, QFileDialog,
                           QMessageBox, QProgressDialog)
from PyQt6.QtCore import Qt
import os
from config import save_config, load_config
from utils import get_random_files, create_output_directory, copy_files

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件随机生成器")
        self.setMinimumWidth(600)

        # 加载配置
        self.config = load_config()

        # 设置中心窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建输入组件
        self.create_input_widgets(layout)

        # 创建生成按钮
        generate_btn = QPushButton("开始生成")
        generate_btn.clicked.connect(self.generate_files)
        layout.addWidget(generate_btn)

    def create_input_widgets(self, layout):
        """创建输入组件"""
        # 视频目录
        video_layout = QHBoxLayout()
        self.video_dir_edit = QLineEdit(self.config['video_dir'])
        video_layout.addWidget(QLabel("视频目录："))
        video_layout.addWidget(self.video_dir_edit)
        video_btn = QPushButton("浏览")
        video_btn.clicked.connect(lambda: self.browse_directory(self.video_dir_edit))
        video_layout.addWidget(video_btn)
        layout.addLayout(video_layout)

        # 文本目录
        text_layout = QHBoxLayout()
        self.text_dir_edit = QLineEdit(self.config['text_dir'])
        text_layout.addWidget(QLabel("文本目录："))
        text_layout.addWidget(self.text_dir_edit)
        text_btn = QPushButton("浏览")
        text_btn.clicked.connect(lambda: self.browse_directory(self.text_dir_edit))
        text_layout.addWidget(text_btn)
        layout.addLayout(text_layout)

        # 视频范围
        video_range_layout = QHBoxLayout()
        self.video_range_edit = QLineEdit(self.config['video_range'])
        video_range_layout.addWidget(QLabel("视频数量范围："))
        video_range_layout.addWidget(self.video_range_edit)
        layout.addLayout(video_range_layout)

        # 文本范围
        text_range_layout = QHBoxLayout()
        self.text_range_edit = QLineEdit(self.config['text_range'])
        text_range_layout.addWidget(QLabel("文本数量范围："))
        text_range_layout.addWidget(self.text_range_edit)
        layout.addLayout(text_range_layout)

        # 生成数量
        count_layout = QHBoxLayout()
        self.output_count_edit = QLineEdit(str(self.config['output_count']))
        count_layout.addWidget(QLabel("生成目录数量："))
        count_layout.addWidget(self.output_count_edit)
        layout.addLayout(count_layout)

        # 输出目录
        output_layout = QHBoxLayout()
        self.output_dir_edit = QLineEdit(self.config['output_dir'])
        output_layout.addWidget(QLabel("输出目录："))
        output_layout.addWidget(self.output_dir_edit)
        output_btn = QPushButton("浏览")
        output_btn.clicked.connect(lambda: self.browse_directory(self.output_dir_edit))
        output_layout.addWidget(output_btn)
        layout.addLayout(output_layout)

    def browse_directory(self, line_edit):
        """浏览并选择目录"""
        directory = QFileDialog.getExistingDirectory(self, "选择目录")
        if directory:
            line_edit.setText(directory)

    def save_current_config(self):
        """保存当前配置"""
        self.config.update({
            'video_dir': self.video_dir_edit.text(),
            'text_dir': self.text_dir_edit.text(),
            'video_range': self.video_range_edit.text(),
            'text_range': self.text_range_edit.text(),
            'output_count': int(self.output_count_edit.text()),
            'output_dir': self.output_dir_edit.text()
        })
        save_config(self.config)

    def generate_files(self):
        """生成文件"""
        try:
            # 保存当前配置
            self.save_current_config()

            # 创建进度对话框
            progress = QProgressDialog("正在生成文件...", "取消", 0, self.config['output_count'], self)
            progress.setWindowModality(Qt.WindowModality.WindowModal)

            for i in range(self.config['output_count']):
                if progress.wasCanceled():
                    break

                # 更新进度
                progress.setValue(i)

                # 创建输出目录
                output_dir = create_output_directory(self.config['output_dir'], i + 1)

                # 获取并复制随机文件
                video_files = get_random_files(self.config['video_dir'], self.config['video_range'])
                text_files = get_random_files(self.config['text_dir'], self.config['text_range'])

                copy_files(self.config['video_dir'], video_files, output_dir)
                copy_files(self.config['text_dir'], text_files, output_dir)

            progress.setValue(self.config['output_count'])
            QMessageBox.information(self, "完成", "文件生成完成！")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成过程中出现错误：{str(e)}")