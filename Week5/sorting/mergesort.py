def mergeSort(nlist):
    if not nlist or len(nlist) < 2:
         return
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    mid = len(nlist) // 2
    left = nlist[:mid]
    right = nlist[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(nlist, left, right)
    print("Merging ", nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

lst = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
mergeSort(lst)