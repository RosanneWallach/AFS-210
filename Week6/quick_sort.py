import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)

def quick_sort_r(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partition_r(a_list, start, end)
    quick_sort_r(a_list, start, pivot-1)
    quick_sort_r(a_list, pivot+1, end)

def quick_sort_m(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partition_m(a_list, start, end)
    quick_sort_m(a_list, start, pivot-1)
    quick_sort_m(a_list, pivot+1, end) 
    
def quick_sort_l(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partition_l(a_list, start, end)
    quick_sort_l(a_list, start, pivot-1)
    quick_sort_l(a_list, pivot+1, end)  

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition_r(a_list, start, end):
    pr = random.randint(start, end)
    a_list[end], a_list[pr] = a_list[pr], a_list[end]
    return partition(a_list, start, end)

def partition_m(a_list, start, end):
    pr = start + (end - start) // 2
    a_list[end], a_list[pr] = a_list[pr], a_list[end]
    return partition(a_list, start, end)

def partition_l(a_list, start, end):
    pr = end
    return partition(a_list, start, end)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot_i = start #random.randint(start, end)
    #pivot = a_list[start]
    pivot = a_list[pivot_i]

    # Start at the first element past the pivot point
    low = pivot_i + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[pivot_i], a_list[high] = a_list[high], a_list[pivot_i]

    return high


print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

#print(myList)
myList1 = myList.copy()
myList2 = myList.copy()
myList3 = myList.copy()
myList4 = myList.copy()


start_time = time.time()
quick_sort(myList1,0,len(myList1)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList1)   

print(f"The execution time is: {end_time-start_time}")


start_time = time.time()
quick_sort_r(myList2,0,len(myList2)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList2)

print(f"The execution time is: {end_time-start_time}")

start_time = time.time()
quick_sort_m(myList3,0,len(myList3)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList3)
print(f"The execution time is: {end_time-start_time}")

start_time = time.time()
quick_sort_l(myList4,0,len(myList4)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList4)  

print(f"The execution time is: {end_time-start_time}")

# There's no winner implementation, the performance is different based on the values distribution
# Any of the implementation can hit the worse case