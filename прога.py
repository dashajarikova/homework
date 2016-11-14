arr = []
while True:
    word =(input('Введите латинское слово: '))
    if not word: break
    elif word[-2:]== 're' or word [-2:]=='ri':
        arr.append(word)
for i in range (len(arr)):
    print (arr[i])
