"""
根据 docs/ 目录下的文件生成 SUMMARY.md 文件
"""

import os
import re


FILE_NAME = os.path.join("docs", "SUMMARY.md")
# 正则匹配：01-xxx 02-xxx 03-xxx
DIR_MATCH = r"\d{2}-\w+"
HEAD_CONTENT = """# Summary

* [介绍](README.md)
* [标签](tags.md)
"""


# 渲染 file 文件
def render(f, dir_list):
    # 将 * [0x-xxx](0x-xxx/README.md) 写入 SUMMARY.md
    f.write(" " * (len(dir_list) - 1) * 4
            + f"* [{dir_list[-1]}]({'/'.join(dir_list)}/README.md)\n")
    # 循环遍历 0x-xxx 目录下的所有文件，直到没有子目录
    new_dir = os.path.join("docs", *dir_list)
    for filename in os.listdir(new_dir):
        new_sub_dir = os.path.join(new_dir, filename)
        # ox-xxx/sub-dir/
        if os.path.isdir(new_sub_dir):
            render(f, dir_list + [filename])
        else:
            # 不将 * [0x-xxx](0x-xxx/README.md) 写入 SUMMARY.md
            if filename == "README.md":
                continue
            # 前面空几个空格是由文件夹层级决定的
            f.write(" " * len(dir_list) * 4
                    + f"* [{filename}]({'/'.join(dir_list)}/{filename})\n")


if __name__ == "__main__":
    # 打开文件
    with open(FILE_NAME, "w", encoding="utf8") as f:
        f.write(HEAD_CONTENT)
        # 获取 docs/ 目录下的所有文件
        for dirname in os.listdir("docs"):
            if not re.match(DIR_MATCH, dirname):
                continue
            # dirname: 0x-xxx
            render(f, [dirname])
