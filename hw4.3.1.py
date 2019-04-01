stringL = input()
length = len(stringL)
stringN = stringL[6: length - 4]
stringNew = stringN.replace("d;","1")
stringNew = stringNew.replace("s;","2")

if "begin" in stringL[0:5]:
    print("begin matched")
else:
    print("missing 'begin'")

if "s" in stringNew[len(stringNew) - 1: len(stringNew)]:
    print("last 's' matched")
else:
    print("the last is not 's'")

if "1" in stringNew[0:1]:
    print("first 'd;' matched")
else:
    print("first is not 'd;'")

i = 0
countD = 0
while i < len(stringNew):
    if stringNew[i: i + 1] is "1":
        countD += 1
    else:
        break
    i += 1

countS = 0
while i <len(stringNew):
    if stringNew[i: i + 1] is "2":
        countS += 1
    else:
        break
    i += 1
if countD + countS == len(stringNew)-1:
    print("num of 'd' is",countD,"and num of 's' is",countS + 1)
else:
    print("sth wrong in input string")

if "end" in stringL[length - 3: length]:
    print("end matched")
else:
    print("missing 'end'")