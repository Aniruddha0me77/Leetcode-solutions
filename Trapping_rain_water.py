def trap(height: list) -> int:
    total = 0
    val = []
    get = 0
    check = {}
    temp = {}
    for i in range(len(height)):
        val.append(height[i])
        j = i+1
        if j < len(height):
            if val[0] > height[j]:
                temp[j] = 1
                get += val[0] - height[j]
            else:
                check.update(temp)
                temp.clear
                total += get
                get = 0
                val.clear()

    
    val.clear()
    get2 = 0  
    for i in range(len(height)-1,-1,-1):
        if i not in check:
            val.append(height[i])
            j = i-1
            if j >= 0:
                if val[0] >= height[j]:
                    get2 += val[0] - height[j]
                else:
                    total += get2
                    get2 = 0
                    val.clear()

    return total