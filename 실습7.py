def sum(n):
    if(n == 101):
        return 1
    else:
        return sum(n-1)+n
    
print("---sum(10)")
print(sum(100))