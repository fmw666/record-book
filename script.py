"""
根据 docs/ 目录下的文件生成 SUMMARY.md 文件
"""

import os


FILE_NAME = os.path.join("docs", "SUMMARY.md")
# 正则匹配：01-xxx 02-xxx 03-xxx
HEAD_CONTENT = """# Summary

* [本文介绍](README.md)
* [标签归档](tags.md)
* [时间归档](date.md)
"""
SKIP_GROUP_LIST = ["styles"]
SKIP_FILENAME_LIST = ["README.md"]
SKIP_DIRNAME_LIST = ["img"]
GROUP_EMOJI_DICT = {
    "计划安排": "🎯",
    "技术文章": "📚",
    "知识笔记": "📝",
    "日常记录": "📖",
    "经验分享": "💡",
}


# 渲染 file 文件
def render(f, dir_list):
    # 将 * [0x-xxx](0x-xxx/README.md) 写入 SUMMARY.md
    f.write(" " * (len(dir_list) - 2) * 4
            + f"* [{dir_list[-1]}]({'/'.join(dir_list)}/README.md)\n")
    # 循环遍历 0x-xxx 目录下的所有文件，直到没有子目录
    new_dir = os.path.join("docs", *dir_list)
    for filename in os.listdir(new_dir):
        if filename in SKIP_FILENAME_LIST or filename in SKIP_DIRNAME_LIST:
            continue
        # ox-xxx/sub-dir/
        new_sub_dir = os.path.join(new_dir, filename)
        if os.path.isdir(new_sub_dir):
            render(f, dir_list + [filename])
        else:
            # 前面空几个空格是由文件夹层级决定的
            f.write(" " * (len(dir_list) - 1) * 4
                    + f"* [{filename}]({'/'.join(dir_list)}/{filename})\n")


if __name__ == "__main__":
    # 打开文件
    with open(FILE_NAME, "w", encoding="utf8") as f:
        f.write(HEAD_CONTENT)
        # 获取 docs/ 目录下的所有文件
        for dirname in os.listdir("docs"):
            # 如果是文件夹，并且不在 SKIP_GROUP_LIST 中
            dirpath = os.path.join("docs", dirname)
            if os.path.isdir(dirpath) \
                    and dirname not in SKIP_GROUP_LIST:
                # dirname: 0x-xxx 将第一层作为 group 写入 f
                if dirname in GROUP_EMOJI_DICT:
                    f.write(f"\n## {GROUP_EMOJI_DICT[dirname]} {dirname}\n\n")
                else:
                    f.write(f"\n## {dirname}\n\n")
                for sub_dirname in os.listdir(dirpath):
                    if sub_dirname in SKIP_FILENAME_LIST or \
                          sub_dirname in SKIP_DIRNAME_LIST:
                        continue
                    new_sub_dir = os.path.join(dirpath, sub_dirname)
                    if os.path.isdir(new_sub_dir):
                        render(f, [dirname, sub_dirname])
                    else:
                        f.write(
                            f"* [{sub_dirname}]({dirname}/{sub_dirname})\n"
                        )
