#Project_1
a=input("ENTER TEXT: \n")
fullstop=0
comma=0
for i in a:
    if i==",":
        comma+=1
    if i==".":
        fullstop+=1
print('Commas used in the string are: ',comma)
print('fullstop used in the string are: ',fullstop)
x=a.replace(',','')
x=x.replace('.','')
b=x.split(' ')
c=set(b)
words=input('Do yo want to know the number of words in the string? Y or N \n')
if words=='Y':
    count_words=len(b)
    print('Number of words used are: ',count_words)
alphabets=input('Do you want to know the number of alphabets used in string? Y or N \n')
count_alphabets=0
if alphabets=='Y':
    for i in a:
        if ord(i)>=65 and ord(i)<=90:
            count_alphabets+=1
        if ord(i)>=97 and ord(i)<=122:
            count_alphabets+=1
    print('Number of Alphabets used are: ',count_alphabets)
frequency=input('Do you want to know the frequency of words ? Y or N \n')
frequency1={}
if frequency=='Y':
    for i in c:
        count=0
        for j in b:
            if i==j:
                count+=1
        frequency1[i]=count
    print('Frequency of words is: \n',frequency1)
capital=input('Do you want to know how many words begin with capital alphabets? Y or N \n')
if capital=='Y':
    count=0
    for i in b:
        if ord(i[0])>=65 and ord(i[0])<=90:
            count+=1
    print('Number of words beginning with capital alphabets are: ',count)
find=input('Do you want to find any word? Y or N \n')
if find=='Y':
    l_find=[]
    find1=input("Enter the word you want to find? \n")
    for i in range(0,len(b)):
        if b[i]==find1:
            l_find.append(i+1)
    print("The position of word is as follows: \n",l_find)

        