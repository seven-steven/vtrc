import json
import os

CONFIG_FILE = "config.json"

def save_config(config):
    """保存配置到文件"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def load_config():
    """加载配置文件"""
    if not os.path.exists(CONFIG_FILE):
        return {
            'video_dir': '',
            'text_dir': '',
            'video_range': '4-6',
            'text_range': '1-1',
            'output_count': 10,
            'output_dir': ''
        }

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)