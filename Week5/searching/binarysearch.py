


def bin_search(lst, search):
    if len(lst) == 0:
        return False
    left = 0
    right = len(lst) - 1
    while left <= right:
        #print(left, right)
        mid = left + (right - left) // 2
        if lst[mid] == search:
            return True
        elif search < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

lst1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
lst2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(bin_search(lst1, 31))
print(bin_search(lst1, 77))
print(bin_search(lst2, "Delta"))
