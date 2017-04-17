import re
import os
def files_kir():
    files =[(f.split('.')[:-1],f) for f in os.listdir('.')]
    files = [f for f in os.listdir('.')if re.search(r'[а-яА-Я]+',f)if os.path.isfile(f)]
    print(len(files))
    return files
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
