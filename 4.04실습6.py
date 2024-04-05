def add(n):
    number = 1
    sum = 0
    while number <= n:
        sum = sum + number
        number = number + 1
    return sum


print("---- add(10)")
print(add(10))
print("---- add(100)")
print(add(100))