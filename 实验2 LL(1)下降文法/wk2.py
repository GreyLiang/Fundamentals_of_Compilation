import re

# int = ( a + b / ( c / d ) ) - char * z

i = 0

def S(strList):
    global i
    V(strList)
    if strList[i] != "=":
        i += 1
        print("定义语句缺失‘ = ’")
    else:
        i += 1
        E(strList)
        if i == len(strList) - 1:
            return True

def E(strList):
    T(strList)
    Ep(strList)

def Ep(strList):
    global i
    if i >= len(strList):
        return
    elif strList[i] == "+" or strList[i] == "-":
        A(strList)
        T(strList)
        Ep(strList)
    else:
        print("Ep 文法出错")
        return

def T(strList):
    F(strList)
    Tp(strList)

def Tp(strList):
    global i
    if i >= len(strList):
        return
    elif strList[i] == "*" or strList[i] == "/":
        M(strList)
        F(strList)
        Tp(strList)
    else:
        print("Tp 文法出错")
        return

def F(strList):
    global i
    if strList[i] == "(":
        i += 1
        E(strList)
        if strList[i] == ")":
            i += 1
    else:
        V(strList)

def A(strList):
    global i
    if strList[i] == "+":
        print("+ 匹配成功")
        i += 1
    elif strList[i] == "-":
        print("- 匹配成功")
        i += 1

def M(strList):
    global i
    if strList[i] == "*":
        print("* 匹配成功")
        i += 1
    elif strList[i] == "/":
        print("/ 匹配成功")
        i += 1

def V(strList):
    global i
    if re.match('^[a-zA-Z]+$',strList[i]):
        print("自定义标识符",strList[i],"命名成功")
        i += 1
    elif re.match('^[a-zA-Z][0-9a-zA-Z]+$',strList[i]):
        print("自定义标识符",strList[i],"命名成功")
        i += 1
    else:
        print("自定义标识符命名失败")
        i += 1

def find_repeat(source, elmt):  # The source may be a list or string.
    ele_index = []
    s_index = 0;
    e_index = len(source)
    while s_index < e_index:
        try:
            temp = source.index(elmt, s_index, e_index)
            ele_index.append(temp)
            s_index = temp + 1
        except ValueError:
            break
    return ele_index

# 从键盘输入
# stringL = input()
# stringL = stringL.split()
# print(stringL,len(stringL))

#从文件中读入
file = open('output.txt', 'r')
stringL = file.read()
print(stringL)
rightK = find_repeat(stringL,')')
charD = find_repeat(stringL,',')
k = 0
while k < len(rightK) - 1:
    if rightK[k] + 1 == rightK[k + 1]:
        rightK = rightK[: k] + rightK[k + 1:]
    k += 1
charList = []
j = 0
while j < len(charD):
    charList.append(stringL[charD[j] + 1: rightK[j]])
    j += 1
print(charList)

if S(charList):
    print("success")
elif i == len(charList):
    print("success")
else:
    print("error")