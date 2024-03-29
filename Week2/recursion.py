
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion
    # Check for stop condition
    if (num > 20):
        return odd_sum
    else:
        if num % 2 == 1:
            odd_sum += num
        # Re-call the function with updating the number with +1
        return loop1Rec(num + 1, odd_sum)

    

def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
    if num < 0:
        return even_sum
    else:
        if num % 2 == 0:
            even_sum += num
        return loop2Rec(num - 1, even_sum)

loop1_res = loop1()
print("Sum of odds between 1 and 20 using 'for' loop =  {}".format(loop1_res))
loop1rec_res = loop1Rec(0, 0)
print("Sum of odds between 1 and 20 using recursion =  {}".format(loop1rec_res))

loop2_res = loop2()
print("Sum of evens between 1 and 20 using 'for' loop =  {}".format(loop2_res))
loop2rec_res = loop2Rec(19, 0)
print("Sum of evens between 1 and 20 using recursion =  {}".format(loop2rec_res))

