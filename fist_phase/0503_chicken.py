for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print("公鸡：%d只,母鸡：%d只, 小鸡：%d只" % (x, y, z))