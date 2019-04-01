f = [1, 1, 1, 1, 1, 1, 1]
g = [1, 1, 1, 1, 1, 1, 1]

def Floyd(strL,i):
    while i < len(strL):
        j = 0
        while j < len(strL):
            if strL[j] == ">" and f[i] <= g[j]:
                temp = g[j]
                f[i] = temp + 1
                j += 1
            elif strL[j] == "<" and f[i] >= g[j]:
                temp = f[i]
                g[j] = temp + 1
                j += 1
            elif strL[j] == "=" and f[i] != g[j]:
                if f[i] > g[j]:
                    temp = f[i]
                    g[j] = temp
                elif f[i] < g[j]:
                    temp = g[j]
                    f[i] = temp
                j += 1
            else:
                j += 1
        i += 1

k = 0
string = [['>','<','<','<','>','<','>'],
          ['>','>','<','<','>','<','>'],
          ['>','>','<','<','>','<','>'],
          ['<','<','<','<','=','<',' '],
          ['>','>','>',' ','>',' ','>'],
          ['>','>','>',' ','>',' ','>'],
          ['>','>','>','>','>','>',' ']]

while k < 7:
    Floyd(string[k],k)
    k += 1
print(f,g)