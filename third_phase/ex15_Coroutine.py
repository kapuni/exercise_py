from time import sleep

# 生成器 - 数据生产者
def countdown_gen(n, consumer):
    consumer.send(None)
    while n > 0:
        consumer.send(n)
        n -= 1
    consumer.send(None)


# 协程 - 数据消费者
def countdown_con():
    while True:
        n = yield
        if n:
            print(f'Countdown{n}')
            sleep(1)
        else:
            print('Countdown Over!')


def main():
    countdown_gen(5, countdown_con())


if __name__ == '__main__':
    main()


"""使用@coroutine装饰器对协程进行预激操作，
不需要再写重复代码来激活协程。"""
# from functools import wraps
#
#
# def coroutine(fn):
#
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         gen = fn(*args, **kwargs)
#         next(gen)
#         return gen
#
#     return wrapper