n = int(input())
sentence = input()

length = len(sentence.split())
chars = sentence.split()
chars.reverse()

if length != n:
    pass
else:
    for i in chars:
        print(i,end=" ")
