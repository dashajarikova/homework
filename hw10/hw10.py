def dictr():
    text=input('Введите текст: ')
    sen_spl=text.split ('.')
    for sentence in sen_spl:
        words=sentence.split()
        dict1={i: len(i) for i in words}
        dict2={sentence: dict1 for sentence in sen_spl}
    print (dict2)
dictr ()
