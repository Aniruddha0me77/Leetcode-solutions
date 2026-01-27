def majorityElement(nums: list) -> int:
        max = len(nums)/2
        map = {}
        
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        key = [k for k,v in map.items() if v > max]
        return key[0]