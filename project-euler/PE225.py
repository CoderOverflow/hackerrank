t1, t2, t3, k = map(int, input().split())

def findsomething(t1,t2,t3,k):
    #kdict = {}
    count=0
    n=1
    while count < k:
        a,b,c = t1,t2,t3
        kkset = set()
        d = 1
        n += 2
        '''
        for seed in kdict:
            if not n % kdict[seed]:
                count += 1
                if count >= k:
                    return n
                n += 2
                break
        '''
        while 1:
            #d = (a + b + c) % n
            #a,b,c = b,c,d
            key = (a, b, c)
            if key in kkset:
                #kdict[k]=n
                count +=1
                break
            else:
                kkset.add(key)
            if a % n == 0:
                break
            a, b, c = b, c, (a + b + c) % n
       
    return n

print(findsomething(t1,t2,t3,k))