def isPowerOfFour(n):
    if n <= 0:
        return False
    while (n != 1):
        if n % 4 != 0:
            return False
        n = n//4
    return True


print(isPowerOfFour(-1))
print(isPowerOfFour(0))
print(isPowerOfFour(1))
print(isPowerOfFour(16))
print(isPowerOfFour(20))
