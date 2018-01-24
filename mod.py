
import quicksort
import newmerge

print "------quicksort output-------------------"
t = [38,42,64,55,27,856,353]
s = [38,42,64,55,27,856,353]
print "unsorted input"
print t
print "sorted output"
quicksort.quickSort(s)
print(s)
print "-------Mergesort output------------------"
print "unsorted input"
print t
print "sorted output"
newmerge.mergeSort(s, 0, len(s) - 1)
for i in range(len(s)):
    print ("%d" % s[i]),
