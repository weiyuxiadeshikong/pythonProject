"""
练习pycharm
作者：wxk
日期：2022年04月04日
"""
import sys
import requests

# print('hello world')
# 命令行编程
# print(sys.argv)
# print(sys.argv[1])

# 三方库的引入
response = requests.get("https://www.baidu.com")
print(response.text)
print("Hello git")
print("Hello world")
print("Hello world2")
print("master test")
print("hot-fix test")
print("push  test")
print("pull  test")
