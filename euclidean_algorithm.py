def nwd(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a
    
print(nwd(666, 420))