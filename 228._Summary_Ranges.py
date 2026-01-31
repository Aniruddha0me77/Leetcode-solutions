def summaryRanges( nums: list[int]) -> list[str]:
        leng = len(nums)
        map = {}
        new = []
        if leng == 0:
            return nums
        for i in range(leng):
            if i not in map:
                not_one = False
                for j in range(i,leng):
                    if j < leng-1:
                        if nums[j]+1 == nums[j+1]:
                            map[j] = 1 
                            not_one = True
                            continue
                        elif not_one:
                            new.append(str(nums[i])+"->"+str(nums[j]))
                            map[j] = 1 
                            not_one = False
                            break
                        else:
                            new.append(str(nums[i]))
                            map[j] = 1 
                            not_one = False
                            break
                    elif not_one:
                        new.append((str(nums[i])+"->"+str(nums[j])))
                        return new
                    else:
                        new.append(str(nums[j]))
                        return new                              