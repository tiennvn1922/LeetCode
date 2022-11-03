def isPowerOfThree(n):
    if n <= 0:
        return False
    while n != 1:
        if n % 3 != 0:
            return False
        n = n//3
    return True


print(isPowerOfThree(-1))
print(isPowerOfThree(0))
print(isPowerOfThree(9))
print(isPowerOfThree(12))
print(isPowerOfThree(1))
