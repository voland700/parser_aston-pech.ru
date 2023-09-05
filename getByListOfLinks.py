from getAstonContent import getAstonContent

list = """
https://aston-pech.ru/product/pech-dlya-bani-aston-20-inox-steklo/
https://aston-pech.ru/product/pech-dlya-bani-aston-12-inox-steklo/
https://aston-pech.ru/product/kamin-aston-600-k-1-talkohlorit/
https://aston-pech.ru/product/pech-otopitelnaya-aston-lesnaya-300/
"""

lines = list.splitlines()
links = []
for line in lines:
    if bool(line):
        links.append(line.strip())



if links:
    amount = len(links)
    print('Получено '+str(amount)+' ссылок для парсинга. Начинаю сбор контента...')
else:
    print('Ссылки для парсинга не получены. Провере скисок ссылок')
    exit()

content = getAstonContent()

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
