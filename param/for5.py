# # Write a programe to findout how letter the word has 
# word=str(input("Enter any word "))
# # word="Param patel"
# count=0

# for i in word:
#     # print(i,end=" ")
#     count=count+1
    
# print(f"total letter are {count}")

string='the orange fox over the lake'

vowels="a"
v2='e'
v3='i'
v4='o'
v5='u'
count=0
ok=[]
ok2=[]
ok3=[]
ok4=[]
ok5=[]
for i in string:
    if i =='a' or i=='e' or i=='i' or i=='o' or i=='u' :
        if i =='a':
            ok.append(i)
        elif i=='e':
            ok2.append(i)
        elif i=='i':
            ok3.append(i)
        elif i=='o':
            ok4.append(i)
        elif i=='u':
            ok5.append(i)
        count+=1
# print(count)
# print(ok,len(ok),ok2,len(ok2),ok3,len(ok3),ok4,len(ok4),ok5,len(ok5))



string='the dhaivat bhatt'
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}

for ok in string:
    for jk in vowels:
        if ok==jk:  
            vowels[jk]=vowels[jk]+1
        
print(vowels)