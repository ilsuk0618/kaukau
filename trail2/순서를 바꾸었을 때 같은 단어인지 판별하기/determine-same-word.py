word1 = input()
word2 = input()

word_1=list(word1)
word_2=list(word2)
word_1.sort()
word_2.sort()
if word_1==word_2:
    print("Yes")
else:
    print("No")