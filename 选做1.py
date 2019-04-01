#某操作系统下合法的文件名规则为：device:name.extention
# 其中第一部分（device:)和第三部分（.extention)可缺省，
# 若 device、name和 extention 都是由字母组成，长度不限，但至少一位

import re

string = input("请输入文件名(回车结束)：")
if len(string) > 0:
    if re.match('^[a-zA-Z][a-zA-Z:][a-zA-Z][.a-zA-Z][a-zA-Z]|[a-zA-Z]|[a-zA-Z][a-zA-Z:][a-zA-Z]|[a-zA-Z][.a-zA-Z][a-zA-Z]+$',string):
        print("文件名合法")
    else:
        print("文件名格式错误")
else:
    print("文件名不能为空")