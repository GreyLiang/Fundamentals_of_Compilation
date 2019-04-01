def beginJug(tokenList):
    if tokenList[0] is "begin":
        i = 1
        if sentenceJug(tokenList[i:],i):
            if tokenList[len(tokenList)] is "end":
                return True
            else:
                print("miss end")
        else:
            print("sentence ERROR in beginJug")
    else:
        print("miss begin")

def sentenceJug(tokenList,i):
    if ifJug(tokenList[i],i):
        print("ifJug matched")
    elif valueJug(tokenList[i],i):
        print("valueJug matched")
    else:
        print("sentenceJug ERROR in sentenceJug")

def ifJug(tokenList,i):
    if tokenList[i] is "if":
        i += 1
        if defineJug(tokenList[i:],i):
            if tokenList[i] is "then":
                i += 1
                if sentenceJug(tokenList[i:],i):
                    print("'if' matched")
                else:
                    print("sentenceJug ERROR in ifJug")
            else:
                print("missing then")
        else:
            print("defineJug ERROR in ifJug")
    else:
        print("missing if")

def valueJug(tokenList,i):
    if "i" in tokenList[i]:
        i += 1
        if ":=" in tokenList[i]:
            i += 1
            if defineJug(tokenList[i:],i):
                return True
            else:
                print("defineJug ERROR in valueJug")
        else:
            print("miss :=")
    else:
        print("sentence not found")

def defineJug(tokenList,i):
    if "i" in tokenList[i]:
        i += 1
        if "+" in tokenList[i]:
            while "+" in tokenList[i] and "i" in tokenList[i + 1]:
                i += 2
        elif "end" in tokenList[i]:
            print("match")
        elif "then" in tokenList[i]:
            print("go into if")
        else:
            print("E ERROR")

'''存放字符和相对序号的列表'''
charList = []#从文件中读取
beginJug(charList)