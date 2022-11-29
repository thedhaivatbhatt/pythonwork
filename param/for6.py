string='the orange fox over the lake'
vowel={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in string:
    for j in vowel:
        if i == j:
            vowel[j]=vowel[j]+1
            
print(vowel)
