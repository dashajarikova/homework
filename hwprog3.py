w = []
while True:
    word =(input('Введите латинское слово: '))
    if not word: break
    elif word[-2:]== 're' or word [-2:]=='ri':
        w.append(word)
for i in range (len(w)):
    print (w[i])
