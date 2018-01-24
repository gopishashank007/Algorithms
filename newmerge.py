

def partition(low,mid,high):
    global n1;
    global n2;
    n1 = mid - low + 1
    n2 = high - mid
    return n1,n2



def merge(s,low,mid,high):

    (n1,n2)= partition(low, mid, high)
    s1 = [0] * (n1)
    s2 = [0] * (n2)

    for i in range(0, n1):
        s1[i] = s[low + i]

    for j in range(0, n2):
        s2[j] = s[mid + 1 + j]


    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if s1[i] <= s2[j]:
            s[k] = s1[i]
            i += 1
        else:
            s[k] = s2[j]
            j += 1
        k += 1

    while i < n1:
        s[k] = s1[i]
        i += 1
        k += 1

    while j < n2:
        s[k] = s2[j]
        j += 1
        k += 1


def mergeSort(s, low, high):
    if low < high:
        mid = (low + (high - 1)) / 2

        mergeSort(s, low, mid)
        mergeSort(s, mid + 1, high)
        merge(s, low, mid, high)


# Driver code to test above

#s = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#n = len(s)
#print ("Given array is")
#for i in range(n):
 #   print ("%d" % s[i]),

#mergeSort(s, 0, n - 1)
#print ("\n\nSorted array is")
#for i in range(n):
 #   print ("%d" % s[i]),
