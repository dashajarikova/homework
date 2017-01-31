import re
def hope():
    with open ('text.txt', 'r', encoding='utf-8') as f:
        text=f.read()
        text=text.lower()
        text=text.strip('.,!?-')
        words=text.split(' ')
        result=[]
        for word in (words):
            find=re.search ('(вып(и(л(а|о|и)|вш(и(й|ми?|е|х)|е(го|му?|е|й|ю)|ая|ую)|т(ы(й|ми?|х|е)?|о(й|ю|е|го|му)?|ая|ую)?)|е(й(те)?)|ь(ю(т)?|(е(т|шь|м)))))',word)
            if find != None:
                 result.append(find.group())
        print (result)
u=hope()
#'Вот формы слова "пить", которые встретились в тексте '+
#result.append(find.group())
