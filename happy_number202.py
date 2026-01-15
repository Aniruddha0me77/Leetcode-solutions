def isHappy(n: int) -> bool:
        check = {}
        num = n
        def elementsquare(num)-> int:
            sum = 0
            if num >= 10:
                sum += (num%10)**2
                new = num//10
                sum += (elementsquare(new))
            else:
                sum += num**2
            return sum
        
        while num != 1 :
            if num not in check:
                check[num] = 1
                num = elementsquare(num)
            else:
                 return False
                 


        if num == 1:
            return True
            

