import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
            #dump - 将Python对象按照JSON格式序列化到文件中
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()

# import requests
# import json
#
#
# def main():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
           ##APIkey
#     data_model = json.loads(resp.text)
#     for news in data_model['newslist']:
#         print(news['title'])
#
#
# if __name__ == '__main__':
#     main()