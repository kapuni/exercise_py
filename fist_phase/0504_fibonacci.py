a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    #right to left; b=1, a+b=1 --> a=1, b=1
    print(a, end=' ')