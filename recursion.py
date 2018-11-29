def fib(n):
     
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) +fib(n-2)
         
def fab(l):
        numbers = []
        [numbers.append(fib(i)) for i in range(l+1)]
        return numbers

def fib2(n):
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b



 

def toStr(n,base):
    rStack = []
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.append(convertString[n])
        else:
            rStack.append(convertString[n % base])
        n = n // base
    res = ""
    while not len(rStack)== 0:
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))




def learn(num,base):
    result = []
    pool = '0123456789ABCDEF'
    while True:
        
        if base > num:
            result.append(pool[num])
            break
        else:
            
                result.append(pool[num % base])
                num = num// base
    res = ''
    while not len(result) == 0:
        res = res + str(result.pop())
    return res


def changes(coinList,change):
    minnum = change
    if change in coinList:
        return 1
    else:
        for i in [c for c in coinList if c <= change]:
            num = 1 + changes(coinList,change - i)
            if minnum > num:
                minnum = num
    return minnum




















 
