arr = []
while True:
    word =(input('Введите латинское слово: '))
    if not word: break
    elif word[-1]== 'e' and word [-2]=='r':
        arr.append(word)
for i in range (len(arr)):
    print (arr[i])
