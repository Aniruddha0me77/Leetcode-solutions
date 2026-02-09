def multiply( num1: str, num2: str):

    #print(len(num1) if len(num1) > len(num2) else len(num2))
    sum = 0
    val = 0
    
    n = 0
    for i in range(len(num1)-1,-1,-1):
        k = 0
        digit = 0
        for j in range(len(num2)-1,-1,-1):
            val = int(num1[i]) * int(num2[j]) + digit
            digit = int(val/10)
            rem = int(val%10)
            if j > 0:
                sum += rem *(10**k)*(10**n)
            else:
                sum += val *(10**k)*(10**n)
            k += 1
        n += 1
    
    stri = str(sum)
    print(type(stri))
    print(stri)


multiply("89","69")
multiply("522","152")
multiply("57565786546787","7484564463")
