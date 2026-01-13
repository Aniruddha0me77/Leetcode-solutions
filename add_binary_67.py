def addBinary(a: str, b: str) -> str:
    
    i = len(a)- 1
    j = len(b) - 1
    s = []
    n = 0
    while (i >= 0) and (j >= 0):
        if (a[i] == '1' and b[j] == '0') or (a[i] == '0' and b[j] == '1'):
            if n == 1:
                s.append('0')
                n = 1
            else:
                s.append('1')
        elif (a[i] == '0' and b[j] == '0'):
            if n == 1:
                s.append('1')
                n = 0
            else:
                s.append('0')
        elif (a[i] == '1' and b[j] == '1'):
            if n == 1:
                s.append('1')
            else:
                s.append('0')
                n = 1
        
        i -= 1
        j -= 1

    if i >= 0 or j >= 0:
        k = i if (i > j) else j
        first = True
        if i < j :
            first = False
        if first:
            for i in range(k,-1,-1):
                    if a[i] == '1':
                        if n == 1:
                            s.append('0')
                        else:
                            s.append('1')
                            n = 0
                    elif a[i] == '0':
                        if n == 1:
                            s.append('1')
                            n = 0
                        else:
                            s.append('0')

        else:
            for i in range(k,-1,-1):
                if b[i] == '1':
                    if n == 1:
                        s.append('0')
                    else:
                        s.append('1')
                        n = 0
                elif b[i] == '0':
                    if n == 1:
                        s.append('1')
                        n = 0
                    else:
                        s.append('0')

    if n == 1:
        s.append('1')

    s.reverse()
    #stri = ''.join(map(str,s))    
    stri = ''.join(s)
    print(stri)
    #print(type(stri))

addBinary("1010","1011")
addBinary("1111","1111")
addBinary("100","110010")