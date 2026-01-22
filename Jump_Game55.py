def canJump(nums: list) -> bool:
    def re(i,val,end) -> list:
        last = i + val + 1
        d = []
        for j in range(i+1,last):
            if j <= end-1:
                d.append(j)
            else:
                break
        return d
    
    dic = {}
    def check(i,l) -> bool:
        arr = re(i,nums[i],len(nums))
        for k in reversed(arr):
            if k not in dic:
                dic[k] = 1
            else:
                continue
            if nums[k] >= (l - k):
                return True
            elif nums[k] != 0:
                if check(k,len(nums)-1):
                    return True

    if len(nums) == 1:
        return True
    elif nums[0] != 0:      
        mew = check(0,len(nums)-1)
        if mew:
            return True            
    return False
        
