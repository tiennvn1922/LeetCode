def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


print(isPowerOfTwo(-1))
print(isPowerOfTwo(0))
print(isPowerOfTwo(1))
print(isPowerOfTwo(8))
print(isPowerOfTwo(10))
