def score(s,m):
    n = 0
    for i in range(len(s)):
        if s[i] == m[i]:
            n += 1
        else:
            pass
    return 1.0*n/len(s)


def counttimes(s):
    import random
    import string
    
    pool = string.ascii_lowercase + ' '
    flag = True
    t = len(s)
    n = 0
    
        
    while flag == True:
        try:
            n += 1
            m = ''
            for i in range(t):
                randi = random.randint(0,26)
                m = m + pool[randi]
                #print('%s letter(s) drawn from the pool %s,%s th'%(str(t),pool[randi],str(randi)))
            scor  = score(s,m)
            #print (s,m,scor)
            
            if scor == 1:
                flag = False
        except IndexError:
            #print('Error after',str(n),'loops',(s,m))
            break
   
    return ('Matched "%s" after %d loops' %(s,n))


