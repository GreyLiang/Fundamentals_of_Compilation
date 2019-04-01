import re

'''定义保留字'''
reservedList = ["void","int","double","float","if","else","for","do","while","switch","case"]
charList = ["(", ")", "[", "]", "{", "}", ",", ";", ":"]
operateList = ["+", "-", "*", "/", "++", "--", "+=", "-=", "*=", "/=", "<", ">", "!", ">=", "<=", "!=", "==", "="]
noteList = ["//","/*","*/"]
otherList = ["&", "|", "&&", "||"]
unsignedList = ["$","￥","@","%","^","~"]

'''存放字符和相对序号的列表'''
stringList = []
numberList = []

'''从文件中读入字符串'''
def readFile():
    string = []
    with open('compile.txt', 'r') as f:
        for line in f:
            string.append(list(map(str, line.split(','))))
        print(string)
    return string

'''定义存放变量以及变量值的列表'''
# storeIntAlp = []
# storeIntNum = []
# storeDoubleAlp = []
# storeDoubleNum = []
# storeFloatAlp = []
# storeFloatNum = []

'''识别定义为变量的语句、识别定义的变量类型'''
# def typeJug(stringTypeIn, i):
#     if "int" in stringTypeIn[i]:
#         if stringTypeIn[i + 1].isalpha():
#             if ";" in stringTypeIn[i + 2]:
#                 print("int value undefined successfully")
#             elif "=" in stringTypeIn[i + 2]:
#                 if";" in stringTypeIn[i + 4]:
#                     if stringTypeIn[i + 3].isdigit():
#                         print("int value defined successfully")
#                         storeIntAlp.append(stringTypeIn[i + 1])
#                         storeIntNum.append(stringTypeIn[i + 3])
#                     else:
#                         print("some trouble in define int")
#                 else:
#                     print("missing space or ';' after define int")
#         else:
#             print("missing alpha in defining int")
#     elif "double" in stringTypeIn[i]:
#         if stringTypeIn[i + 1].isalpha():
#             if ";" in stringTypeIn[i + 2]:
#                 print("double value undefined successfully")
#             elif "=" in stringTypeIn[i + 2]:
#                 if ";" in stringTypeIn[i + 4]:
#                     if stringTypeIn[i + 3].isdigit():
#                         print("double value defined successfully")
#                         storeDoubleAlp.append(stringTypeIn[i + 1])
#                         storeDoubleNum.append(stringTypeIn[i + 3])
#                     else:
#                         print("some trouble in define double")
#                 else:
#                     print("missing space or ';' after define double")
#         else:
#             print("missing alpha in defining double")
#     elif "float" in stringTypeIn[i]:
#         if stringTypeIn[i + 1].isalpha():
#             if ";" in stringTypeIn[i + 2]:
#                 print("float value undefined successfully")
#             elif "=" in stringTypeIn[i + 2]:
#                 if ";" in stringTypeIn[i + 4]:
#                     if stringTypeIn[i + 3].isdigit():
#                         print("float value defined successfully")
#                         storeFloatAlp.append(stringTypeIn[i + 1])
#                         storeFloatNum.append(stringTypeIn[i + 3])
#                     else:
#                         print("some trouble in define float")
#                 else:
#                     print("missing space or ';' after define float")
#         else:
#             print("missing alpha in defining float")

'''识别保留字reservedList'''
def reserveJug(stringTypeIn, i):
    if "void" in stringTypeIn[i]:
        stringList.append("void")
        numberList.append(1)
    elif "int" in stringTypeIn[i]:
        stringList.append("int")
        numberList.append(2)
    elif "double" in stringTypeIn[i]:
        stringList.append("double")
        numberList.append(3)
    elif "float" in stringTypeIn[i]:
        stringList.append("float")
        numberList.append(4)
    elif "if" in stringTypeIn[i]:
        stringList.append("if")
        numberList.append(5)
    elif "else" in stringTypeIn[i]:
        stringList.append("else")
        numberList.append(6)
    elif "for" in stringTypeIn[i]:
        stringList.append("for")
        numberList.append(7)
    elif "do" in stringTypeIn[i]:
        stringList.append("do")
        numberList.append(8)
    elif "while" in stringTypeIn[i]:
        stringList.append("while")
        numberList.append(9)
    elif "switch" in stringTypeIn[i]:
        stringList.append("switch")
        numberList.append(10)
    elif "case" in stringTypeIn[i]:
        stringList.append("case")
        numberList.append(11)

'''识别纯数字'''
def digitJug(stringIn,i):
    if re.match('^[0-9]+$',stringIn[i]):
        return True
    else:
        return False

'''识别以字母开头的字母数字组合'''
def alphaJug(stringIn,i):
    if re.match('^[a-zA-Z]+$',stringIn[i]):
        return True
    elif re.match('^[a-zA-Z][0-9a-zA-Z]+$',stringIn[i]):
        return True
    #若以数字开头则打印相应错误
    elif re.match('^[0-9][a-zA-Z]+$',stringIn[i]):
        print("wrong in identify the value name")
        return False
    else:
        return False

'''识别符号charList'''
def charJug(stringIn,i):
    if "(" in stringIn[i]:
        stringList.append("(")
        numberList.append(12)
    elif ")" in stringIn[i]:
        stringList.append(")")
        numberList.append(13)
    elif "{" in stringIn[i]:
        stringList.append("{")
        numberList.append(14)
    elif "}" in stringIn[i]:
        stringList.append("}")
        numberList.append(15)
    elif "[" in stringIn[i]:
        stringList.append("[")
        numberList.append(16)
    elif "]" in stringIn[i]:
        stringList.append("]")
        numberList.append(17)
    elif ";" in stringIn[i]:
        stringList.append(";")
        numberList.append(18)
    elif "," in stringIn[i]:
        stringList.append(",")
        numberList.append(19)
    elif ":" in stringIn[i]:
        stringList.append(":")
        numberList.append(20)

'''识别操作operateList'''
def operateJug(stringIn, i):
    if "+=" in stringIn[i]:
        stringList.append("+=")
        numberList.append(41)
    elif "-=" in stringIn[i]:
        stringList.append("-=")
        numberList.append(42)
    elif "*=" in stringIn[i]:
        stringList.append("*=")
        numberList.append(43)
    elif "/=" in stringIn[i]:
        stringList.append("/=")
        numberList.append(44)
    elif "++" in stringIn[i]:
        stringList.append("++")
        numberList.append(35)
    elif "--" in stringIn[i]:
        stringList.append("--")
        numberList.append(36)

    elif ">=" in stringIn[i]:
        stringList.append(">=")
        numberList.append(31)
    elif "<=" in stringIn[i]:
        stringList.append("<=")
        numberList.append(32)
    elif "==" in stringIn[i]:
        stringList.append("==")
        numberList.append(33)
    elif "!=" in stringIn[i]:
        stringList.append("!=")
        numberList.append(34)

    elif "+" in stringIn[i]:
        stringList.append("+")
        numberList.append(27)
    elif "-" in stringIn[i]:
        stringList.append("-")
        numberList.append(28)
    elif "*" in stringIn[i]:
        stringList.append("*")
        numberList.append(29)
    elif "/" in stringIn[i]:
        stringList.append("/")
        numberList.append(30)

    elif ">" in stringIn[i]:
        stringList.append(">")
        numberList.append(23)
    elif "<" in stringIn[i]:
        stringList.append("<")
        numberList.append(24)
    elif "=" in stringIn[i]:
        stringList.append("=")
        numberList.append(25)
    elif "!" in stringIn[i]:
        stringList.append("!")
        numberList.append(26)

'''识别注释noteList'''
def noteJug(stringIn,i):
    if "//" in stringIn[i]:
        stringList.append("//")
        numberList.append(45)
    elif "/*" in stringIn[i]:
        stringList.append("/*")
        numberList.append(46)
    elif "*/" in stringIn[i]:
        stringList.append("*/")
        numberList.append(47)

'''识别其他otherList'''
def otherJug(stringIn,i):
    if "&&" in stringIn[i]:
        stringList.append("&&")
        numberList.append(38)
    elif "||" in stringIn[i]:
        stringList.append("||")
        numberList.append(40)
    elif "&" in stringIn[i]:
        stringList.append("&")
        numberList.append(37)
    elif "|" in stringIn[i]:
        stringList.append("|")
        numberList.append(39)

'''删除注释'''
def delComments(numberL,stringL):
    i = 0
    commentsHead = []
    commentsTail = []
    while i < len(numberL):
        if numberL[i] is 46:
            commentsHead.append(i)
        elif numberL[i] is 47:
            commentsTail.append(i)
        i += 1
    i = 0
    while i < len(commentsHead):
        if numberL[i] is "":
            break
        print("Comments", i+1, "Starts at", commentsHead[i], "End with", commentsTail[i])
        del numberL[commentsHead[i] : commentsTail[i] + 1]
        del stringL[commentsHead[i] : commentsTail[i] + 1]
        i += 1

'''判断输入语句正确性'''
def grammarJug():
    # 赋值语句、定义语句、条件语句、循环语句
    return True

'''字符种类判断'''
def typeJug(stringNew,n):
    listingNum = 0
    #对每个字符判断
    while listingNum < len(stringNew) - 1:
        if stringNew[listingNum] in reservedList:
            reserveJug(stringNew,listingNum)
        elif stringNew[listingNum] in charList:
            charJug(stringNew,listingNum)
        elif stringNew[listingNum] in operateList:
            operateJug(stringNew,listingNum)
        elif stringNew[listingNum] in noteList:
            noteJug(stringNew,listingNum)
        elif stringNew[listingNum] in otherList:
            otherJug(stringNew,listingNum)
        elif alphaJug(stringNew,listingNum):
            stringList.append(stringNew[listingNum])
            numberList.append(21)
        elif digitJug(stringNew,listingNum):
            stringList.append(stringNew[listingNum])
            numberList.append(22)
        #判断不可识别的字符、输出相应错误信息
        else:
            print("Unrecognizable symbol '" + stringNew[listingNum] + "' appeared in line " + str(n + 1))
        listingNum += 1

'''读入、判断'''
string = []
#从文件中读入字符串
with open('read.txt', 'r') as f:
    for line in f:
        string.append(list(map(str, line.split(','))))
print(string)
length = len(string)
n = 0
# 将文件中读入的每一行分别处理并判断字符
while n < length:
    stringNew = string[n]
    stringNew = str(stringNew).replace("['","")
    stringNew = stringNew.replace("']","")
    stringNew = stringNew.replace("\\n"," ")
    stringNew = stringNew.replace("\\t"," ")
    stringNew = stringNew.split()
    stringNew.append(" ")
    print(stringNew,n)
    typeJug(stringNew,n)
    n += 1

'''将两个列表写出到文件中'''
#删除注释中的内容
delComments(numberList,stringList)

#打开文件开始写入
f = open("output.txt", "w+")

#写入对应的保留字及序号
j = 0
while j < len(numberList):
    f.write("("+str(numberList[j])+","+stringList[j]+")")
    j += 1