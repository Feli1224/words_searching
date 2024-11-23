import sys
import os
import re

# 定义高亮关键词的函数
def highlight_keyword(sentence, keyword):
    highlighted = re.escape(keyword)
    pattern = f"({highlighted})"
    highlighted_sentence = re.sub(pattern, r"\033[34m\g<1>\033[0m", sentence)  # 高亮显示关键词
    return highlighted_sentence

if getattr(sys, 'frozen', False):
    corpus_dir_path = os.path.join(sys._MEIPASS, '朱氏语料库')
else:
    corpus_dir_path = os.path.join(os.getcwd(), '朱氏语料库')

def read_file_with_encoding(file_path):
    encodings = ['gbk', 'gb2312', 'gb18030']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read(), encoding
        except UnicodeDecodeError:
            pass
        except Exception as e:
            pass
    return None, None

def search_in_files(keyword, dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_content, encoding = read_file_with_encoding(file_path)
            if file_content is not None:
                sentences = file_content.splitlines()  # 将文件内容按行分割成句子
                for line_number, sentence in enumerate(sentences, 1):
                    if keyword in sentence:
                        highlighted_sentence = highlight_keyword(sentence, keyword)
                        print(f"文件：{file_path}，编码：{encoding}，行号：{line_number}，内容：{highlighted_sentence}")

def main():
    keyword = input("请输入要搜索的关键词：")
    search_in_files(keyword, corpus_dir_path)

if __name__ == '__main__':
    main()