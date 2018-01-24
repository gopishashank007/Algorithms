#program for implementing quicksort
import random

#class quickly:

def quickSort(s):
    n=(len(s)-1)
    inplacequicksort(s,0,n)


def inplacequicksort(s,a,b):
    if a < b:
        l=inPlacePartition(s, a, b)
        inplacequicksort(s,a,l-1)
        inplacequicksort(s,l+1,b)

def inPlacePartition(s,a,b):
    #generating a random number
    r=random.randint(0,len(s))
    #swapping random and last position
    #temp=s[r]
    #s[r]=s[b]
    #s[b]=temp
    #initilazing the pivot
    p=s[a]
    #defining left and right
    le=a+1
    re=b
    #print "le is",le
    #print "re is",re

    while (le<=re):
    #finding the element smaller than the pivot

        while le<=re and s[le]<=p:
            le=le+1

        while s[re]>=p and le<=re:
            re=re-1

        if le<re:
            temp=s[le]
            s[le]=s[re]
            s[re]=temp
        #print temp
    temp = s[a]
    s[a] = s[re]
    s[re] = temp

    return re


#s = [54,26,93,17,77,31,44,55,20]
#quickSort(s)
#print(s)
