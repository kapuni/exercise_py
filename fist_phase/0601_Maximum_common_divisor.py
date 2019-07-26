
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):                  #x --> 0 倒着取
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


if __name__ == '__main__':
    x = int(input('x:'))
    y = int(input('y:'))
    g = gcd(x, y)
    print(g)
    print(lcm(x,y))
