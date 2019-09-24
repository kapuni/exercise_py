import pandas

data = pandas.read_csv(
    'D:/PDABook/第四章/4.3.3 字符转时间/字符转时间.csv',
    engine='python', encoding='utf-8'
)
#print(data.注册时间.dtype)

data['时间'] = pandas.to_datetime(
        data.注册时间,
        format='%Y/%m/%d'
        )
data['年月'] = data.时间.dt.strftime('%Y-%m')
print(data['时间'].dtype)