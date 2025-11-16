# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 读取原文件内容
with open('random_int.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 处理内容：将非保留字的小写转为大写
processed_content = []
words = content.split()
for word in words:
    if word in reserved_words:
        processed_content.append(word)
    else:
        processed_content.append(word.upper())
# 还原为带空格的内容
processed_content = ' '.join(processed_content)

# 写入新文件
with open('converted_random_int.py', 'w', encoding='utf-8') as f:
    f.write(processed_content)

print("文件转换完成，结果已保存到 converted_random_int.py")
