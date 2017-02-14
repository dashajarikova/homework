import re
def change():
    with open ('text.txt', 'r', encoding='utf-8') as source:
        old_text=source.readlines()
    with open ('endtext.txt', 'w', encoding='utf-8') as f:
        for line in old_text:
            newline=re.sub(r'(\s|\(|«)?философи((я|и|ю|е)(м|й|ю|х)?и?(\s|.|,|:|;)?(\[|\s|\)|»))', r'\1астрологи\2', line, flags=re.DOTALL)
            newnewline=re.sub(r'(\s|\(|«)?Философия((а|о|у|е|ы)?(м|в|х)?и?(\s|.|,|:|;)?(\[|\s|»))', r'\1Астрологи\2', newline, flags=re.DOTALL)
            f.write(newnewline)
    return 'Сделано!'

change()
