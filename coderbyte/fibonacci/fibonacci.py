import math


def f(num):
    if num == 0 or num == 1:
        return num
    a = 0
    b = 1
    cur = 0
    for i in range(0, num - 2 + 1):
        cur = a + b
        a = b
        b = cur
    return cur


def is_num_fibonacci(target):
    a, b, c = 0, 1, 1
    while a < target:
        c = a + b
        a = b
        b = c
    if a == target:
        return True
    else:
        return False


def is_fibonacci_series(arr):
    for v in arr:
        if not is_num_fibonacci2(v):
            return False
    return True


def is_perfect_square(num):
    s = int(math.sqrt(num))
    return s * s == num


def is_num_fibonacci2(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


if __name__ == '__main__':
    print(f(10))
    print(is_num_fibonacci(0))
    print(is_num_fibonacci2(55))
    print(is_fibonacci_series([2, 3, 5]))
