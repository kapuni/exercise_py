"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
"""
def fib(num, temp={}):
    """用递归计算Fibonacci数"""
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]

def main():
    items = list(map(int, input().split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(overall[0])


if __name__ == '__main__':
    main()