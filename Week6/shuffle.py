import random
# Time complexity is: O(n)
# Because we have one loop over the list of size n

def shuffle(lst):
    for i in range(len(lst)):
        new_i = random.randint(0, i)
        if i != new_i:
            lst[i], lst[new_i] = lst[new_i], lst[i]
    return lst


lst = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print("Before Shuffle:")
print(lst)

print("Shuffled:")

lst = shuffle(lst)
print(lst)
lst = shuffle(lst)
print(lst)
lst = shuffle(lst)
print(lst)
lst = shuffle(lst)
print(lst)
lst = shuffle(lst)
print(lst)