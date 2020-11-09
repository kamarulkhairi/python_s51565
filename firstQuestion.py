def countingbits(n):
    count = 0
    while n:
        count += 1
        n >>= 1

    return count


i = int(input('enter a number'))
print(countingbits(i))
