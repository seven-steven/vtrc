import os
import random
import shutil
from typing import List, Tuple

def parse_range(range_str: str) -> Tuple[int, int]:
    """解析范围字符串，如 "4-6" -> (4, 6)"""
    start, end = map(int, range_str.split('-'))
    return start, end

def get_random_files(directory: str, count_range: str) -> List[str]:
    """从目录中随机选择指定范围数量的文件"""
    if not os.path.exists(directory):
        return []

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        return []

    min_count, max_count = parse_range(count_range)
    count = random.randint(min_count, max_count)
    count = min(count, len(files))

    return random.sample(files, count)

def create_output_directory(base_dir: str, index: int) -> str:
    """创建输出目录"""
    output_dir = os.path.join(base_dir, str(index))
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def copy_files(src_dir: str, files: List[str], dst_dir: str):
    """复制文件到目标目录"""
    for file in files:
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        shutil.copy2(src_path, dst_path)