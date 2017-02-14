import re
def oh():
    lines=int()
    with open ('text.txt', 'r', encoding='utf-8') as first:
        old_text=first.readlines()
        for line in old_text:
            if '</teiHeader>' in line:
                break
            else:
                lines+=1
    with open ('endtext.txt', 'w', encoding='utf-8') as second:
        lines1=str(lines)
        second.write(lines1)
def oops():
    slov={}
    with open ('text.txt', 'r', encoding='utf-8') as first:
        old_text=first.readlines()
        for line in old_text:
            if "<w lemma=" in line:
                find=re.search ('type=\"(.*)\"',line)
                if find.group(1) in slov:
                    slov[find.group(1)]+=1
                else:
                    slov[find.group(1)]=1
            else:
                continue
    with open ('endtext.txt', 'w', encoding='utf-8') as second:
        for k in slov:
            second.write(k+' ' + str(slov[k])+' \n')
u=oops()

