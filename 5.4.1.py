# coding=utf-8
# 代码文件: ch05/ch5_4_1.py
# 计算水仙花数。提示：水仙花数是一个三位数，三位数各位的立方之和等于三位数本身。

i = 100; r = 0; s = 0; t = 0

while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print("i = " + str(i))

    i += 1

