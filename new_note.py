# -*- coding: utf-8 -*-
"""一键生成当天的论文笔记文件夹和 notebook。

用法:
    python new_note.py "主题"            # 文件夹名: 7.18主题
    python new_note.py "主题" --date 7.20 # 指定日期
"""
import argparse
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "templates" / "paper_note_template.ipynb"


def main():
    parser = argparse.ArgumentParser(description="新建当天的论文笔记")
    parser.add_argument("topic", help="当天主题，用于文件夹命名")
    parser.add_argument("--date", default=None, help="日期，形如 7.18，默认今天")
    args = parser.parse_args()

    today = args.date or f"{date.today().month}.{date.today().day}"
    folder = ROOT / f"{today}{args.topic}"
    folder.mkdir(exist_ok=True)

    dest = folder / "note.ipynb"
    if dest.exists():
        print(f"已存在，跳过: {dest}")
    else:
        shutil.copy(TEMPLATE, dest)
        print(f"已创建: {dest}")
    print("别忘了把今天的 PDF 也放进这个文件夹，并在 README 索引表加一行。")


if __name__ == "__main__":
    main()
