#列表
#import sys
# # #
# # #
# # # def main():
# # #     f = [x for x in range(1, 10)]
# # #     print(f)
# # #     f = [x + y for x in 'ABCDE' for y in '1234567']
# # #     print(f)
# # #     # 用列表的生成表达式语法创建列表容器
# # #     # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
# # #     f = [x ** 2 for x in range(1, 1000)]
# # #     print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# # #     print(f)
# # #     # 请注意下面的代码创建的不是一个列表而是一个生成器对象
# # #     # 通过生成器可以获取到数据但它不占用额外的空间存储数据
# # #     # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
# # #     f = (x ** 2 for x in range(1, 1000))
# # #     print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# # #     print(f)
# # #     for val in f:
# # #         print(val)
# # #
# # #
# # # if __name__ == '__main__':
# # #     main()


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# def main():
#     for val in fib(20):
#         print(val)
#

#元祖
def main():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的, 元祖无法修改其中元素
    person[0] = '李小龙'
    person[1] = 25
    print(person)

    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)

if __name__ == '__main__':
    main()
