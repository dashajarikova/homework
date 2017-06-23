import os
import re
def sents():
    news = 'news'
    sent = {}
    for n in os.listdir(news):
        with open(os.path.join(news, n), encoding='cp1251') as text:
            text = text.read()
            sent[n] = len(re.findall('<se>?(.|\n)+</se>?', text))
#            print(sent)
    return (sent)
def new (sent):
#    print (sent)
    with open('new_file', 'w', encoding = 'utf-8') as new:
        for s in sent:
            new.write(s+'\t'+str(sent[s])+'\n')
new(sents())
