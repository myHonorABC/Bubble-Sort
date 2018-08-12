import time

def bubble(alist):
    n=len(alist)
    for i in range(n-1):
        count=0
        for j in range(n-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                count+=1
        if count==0:
            return


if __name__=='__main__':
    alist=[12,2,53,1,7,2,1,30]
    start=time.time()
    bubble(alist)
    t=time.time()-start
    print(alist)
    print(t)
