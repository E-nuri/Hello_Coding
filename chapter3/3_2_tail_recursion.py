def recursion_factorial(n):
    print(n)
    if n > 1:
        return n * recursion_factorial(n-1)
    elif n == 1:
        return 1


def tail_recursion_factorial(n, result):
    print(result)
    if n == 1:
        return result
    return tail_recursion_factorial(n - 1, result * n)


# print("결과: ", recursion_factorial(100000000000000000))
print("결과: ", tail_recursion_factorial(10000000000000,1))

