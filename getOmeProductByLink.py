from getAstonContent import getAstonContent

content = getAstonContent()

#url= input("Укажите ссылку на страницу товара на сайте aston.ru : ")
url = 'https://aston-pech.ru/product/pech-dlya-bani-aston-20-inox-steklo/'
item = content.getItem(url)
data = []
data.append(item)

print(data)

print('Старт парсинга')
if bool(data):
    content.getExel(data)
    print('Данные товара успешно получены')
else:
    print('Не получается получить данные товара. Проверкти указанную ссылку')
    exit()



