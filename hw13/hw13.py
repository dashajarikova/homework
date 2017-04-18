$import re
import os
def files_kir():
    files_all =[(f.split('.')[:-1],f) for f in os.listdir('.')]
    files = [f for f in files_all if re.search(r'[а-яА-Я]+$',f) if os.path.isfile(f)]
    print(len(files))
files_kir()

def printed():
    all_=[f for f in os.listdir('.')]
    files=[]
    for f in all_:
        if f not in files:
           files.append(f)
        else:
            None
    print(files)
printed()
#как сделать названия без повторений, не знаю(
