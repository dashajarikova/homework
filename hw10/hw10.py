def dictr():
    text=input('Введите текст: ')
    sen_spl=text.split ('.')
    words=text.split()
    dict1={i: len(i) for i in words}
    dict2={a : dict1 for a in sen_spl}
    print (dict2)
dictr ()
