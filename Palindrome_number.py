#question no 9
def  isPalindrome(x: int) -> bool:
    x = str(x)
    left = []
    right = ""

    for i in range(len(x)-1,-1,-1):
        left.append(x[i])
        right.join(x[i])
    for i in range(len(x)):
        right += left[i]
    print(x)
    print(right)
    if right == x:
        print(True)
    else:
        print(False)

    pass

isPalindrome(57275)