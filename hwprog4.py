word=input("Введите слово: ")
n=[]
for i in range(len(word)):
	n=word[len(word)-i:]
	n+=word[i:]
	print(n)
