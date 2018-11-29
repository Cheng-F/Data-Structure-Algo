
def bubble(numlist):
    for i in range(len(numlist)-1,0,-1):
        for j in range(i):
            if numlist[j] > numlist[j+1]:
                numlist[j],numlist[j+1] = numlist[j+1],numlist[j]
    return numlist

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1
    return alist

def mergeSort(alist):
    slist = []
    if len(alist) <= 1:
        slist = alist
        return slist
    else:
        mid = int(len(alist)/2)
        llist = mergeSort(alist[:mid])
        rlist = mergeSort(alist[mid:])
        #print(llist,rlist)
        i = 0
        j = 0
        while i <(len(llist)) and j <(len(rlist)):
            if llist[i] < rlist[j]:
                slist.append(llist[i])
                i += 1
                #print ('i',slist)
            else:
                slist.append(rlist[j])
                j += 1
                #print ('j',slist)
    slist.extend(llist[i:])
    slist.extend(rlist[j:])
    return slist
mergeSort([20, 30, 240, 150, 60, 70, 80, 90, 100, 110])

def insertSort(alist):
    for j in range(1,len(alist),1):
        i = j - 1
        found = False
        new = alist[j]
        ##if alist[j] is the smallest number
        if alist[0] > alist[j]:
                alist[0],alist[j] = alist[j],alist[0]
                new = alist[j]
                        
        while alist[j] < alist[i]:
      
            i -= 1
            for l in range(1,i,1):
                if alist[l] < alist[j] and alist[l+1] > alist[j]:
                    i = l
             
        if i < j-1:
            for k in range(j,i+1,-1):
                alist[k] = alist[k-1]
            alist[i+1] = new
       
    return alist

def insert2(alist):
    for j in range(1,len(alist)):
        key = alist[j]
        i = j-1
        while i>= 0 and alist[i] > key:
            alist[i+1] = alist[i]
            i -= 1
        alist[i+1] = key

    return alist
                    
            
insert2([20, 30, 240, 150, 60, 10, 80, 9, 100, 110])

def shellSort(alist,n):
    a = [[] for x in range(n)]
    num_per_list = int(len(alist)/n)
    prefinal = []
    for m in range(n):
        a[m].extend(alist[i*n+m] for i in range(num_per_list))
        insert2(a[m])
    for i in range(num_per_list):
        for j in range(n):
            prefinal.append(a[j][i])
    return insert2(prefinal)


def shellSort2(alist):
    num_per_list = len(alist)//2
    gap = 2
    while num_per_list >0:
        
        gap = gap * 2
        for i in range(num_per_list):
            gapInsertSort(alist,i,num_per_list)
        num_per_list = (num_per_list)//2
    return alist

def gapInsertSort(alist,i,gap):
    for j in range(i+gap,len(alist),gap):
       # l  = j - gap
        new = alist[j]
        l = j
        while l -gap>=0 and alist[l-gap] > new:
            
            #if l - gap > 0:
                alist[l] = alist[l-gap]
                l -= gap
           # else:
                #alist[l+gap] = alist[l]
                #break
        alist[l] = new
##    for i in range(start+gap,len(alist),gap):
##
##        currentvalue = alist[i]
##        position = i
##
##        while position>=gap and alist[position-gap]>currentvalue:
##            alist[position]=alist[position-gap]
##            position = position-gap
##
##        alist[position]=currentvalue
##    
##

def quickSort(alist):
    fp = alist[0]
    lp = alist[-1]
    mp = alist[int(len(alist)/2)]
    pivot_point = sorted([fp,lp,mp])[1]
    
    if alist.index(pivot_point) == 0:
        left_index = 1
        right_index = len(alist)-1
    elif alist.index(pivot_point) == len(alist)-1:
        left_index = 0
        right_index = len(alist)-2
    else:
        left_index = 0
        right_index = len(alist)-1
    lmark = left_index
    rmark = right_index
    meet = False   
    while not meet:
        if alist[left_index] > pivot_point:
            lmark = left_index
        else:
            left_index += 1
        if alist[right_index] < pivot_point:
            rmark = right_index
        else:
            right_index -= 1
        if lmark < rmark:
            
            alist[lmark],alist[rmark] = alist[rmark],alist[lmark]
            left_index = lmark
            right_index = rmark
        else:
            meet = True
    return left_index

quickSort([54,26,93,17,77,31,44,55,20])
        

    
        
    
















