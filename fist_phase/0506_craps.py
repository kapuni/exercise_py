from random import randint

name = str(input('输入你的名字：'))
money = 1000
while money > 0:
    print(name, '的总资产为：', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print(name,  '摇出了%d点' % first)
    if first == 7 or first == 11:
        print(name, '胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜！')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print(name, '摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print(name, '胜')
            money += debt
            needs_go_on = False
print('你破产了')
