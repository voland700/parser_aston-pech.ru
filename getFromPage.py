from getAstonContent import getAstonContent

content = getAstonContent()

url= input("Укажите ссылку на страницу категории товаров сайта aston.ru : ")

links = content.getLinksFromPageCategory(url)

if links:
    amount = len(links)
    print('Получено '+str(amount)+' ссылок для парсинга. Начинаю сбор контента...')
else:
    print('Ссылки для парсинга не получены. Проверкти указанную ссылку')
    exit()


data = []
missing = []
missingCount = 0
findCount = 0
for link in links:
    item = content.getItem(link)
    if not bool(link):
        missingCount +=1
        missing.append(link)

    data.append(item)
    findCount+=1

content.getExel(data)

print('**************** --- END! --- ***************')

if findCount == len(links):
    print('Успешно получен контент '+str(findCount)+" товаров")
elif findCount > 0 and missingCount > 0:
    print('Успешно получен контент ' +str(findCount) + " товаров")
    print('Не получены товары по ' + +str(len(missingCount)) + "ссылкам:")
    for missingLink in missing:
        print(missingLink)
elif missingCount == 0:
    print('Не удачный парсинг контента, неудалось получить данные '+ str(len(links)) +' товаров')






