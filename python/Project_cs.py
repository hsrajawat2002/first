#Project_1
#2020UEE0123 Harshvardhan Singh
print(' \n \n ')
print('#PROJECT by 2020UEE0123  \nApplying Multiple functions on a given text for the ease of USER')
a=input("ENTER TEXT: ")
fullstop=0
comma=0
for i in a:
    if i==",":
        comma+=1
    if i==".":
        fullstop+=1
print('Commas used in the string are: ',comma)
print('fullstop used in the string are: ',fullstop)
#TASK1= finding number of fullstops and commas
x=a.replace(',','')          
x=x.replace('.','')
x=x.replace('?','')
b=x.split(' ')
c=set(b)
#TASK2= finding number of words
print(' \n \n ')
words=input('Do yo want to know the number of words in the string? \nY or N \n') 
if words=='Y':
    count_words=len(b)
    print('Number of words used are: ',count_words)
#TASK3= number of alphabets
print(' \n \n ')
alphabets=input('Do you want to know the number of alphabets used in string? \nY or N \n') 
count_alphabets=0
if alphabets=='Y':
    for i in a:
        if ord(i)>=65 and ord(i)<=90:
            count_alphabets+=1
        if ord(i)>=97 and ord(i)<=122:
            count_alphabets+=1
    print('Number of Alphabets used are: ',count_alphabets)
#TASK4= frequency of words
print(' \n \n ')
frequency=input('Do you want to know the frequency of words ? \nY or N \n') 
frequency1={}
for i in c:
        count=0
        for j in b:
            if i==j:
                count+=1
        frequency1[i]=count
if frequency=='Y':
    print('Frequency of words is: \n',frequency1)
#Task5= number of words beginning with capital alphabet
print(' \n \n ')
capital=input('Do you want to know how many words begin with capital alphabets? \nY or N \n') 
if capital=='Y':
    count=0
    for i in b:
        if ord(i[0])>=65 and ord(i[0])<=90:
            count+=1
    print('Number of words beginning with capital alphabets are: ',count)
#TASK6= Finding position of word
print(' \n \n ')
find=input('Do you want to find any word? \nY or N \n') 
if find=='Y':
    l_find=[]
    find1=input("Enter the word you want to find? \n")
    for i in range(0,len(b)):
        if b[i]==find1:
            l_find.append(i+1) 
    if len(l_find)>0:
        print("The position of word is as follows: \n",l_find)
    else:
        print('The word does not exist in the text.') 
'''We are giving position of word which is user friendly 
ex. anand is a very good boy, then here position of 'is' will be 2 instead of giving position
in technical terms like position will be 6, program should be simple for the user  '''
#TASK7= reversing of string
print(' \n \n ')
reversing=input('Do you want to see the reversed form of text? \nY or N \n') 
if reversing=='Y':
    reversing1=''
    for i in range(len(a)-1,-1,-1):
        reversing1=reversing1 + a[i]
    print('Reversed form of the Text is:\n',reversing1)
#TASK8= sorting string in terms of alphabets and consonents
print(' \n \n ')
sorting=input('Do you want to find the number of vowels and consonents used in the text? \nY or N\n')
if sorting=='Y':
    vowels=0
    consonents=0
    blank=[65,69,73,79,85,97,101,105,111,117]
    for i in x:
        if ord(i)>=65 and ord(i)<=90:
            if ord(i) in blank:
                vowels+=1
            else:
                consonents+=1
        if ord(i)>=97 and ord(i)<=122:
            if ord(i) in blank:
                vowels+=1
            else:
                consonents+=1
    print('The total number of vowels in text are: ',vowels)
    print('The total number of consonents in text are: ',consonents)
#TASK9 = representing text in ascci format
print(' \n \n ')
asci=input('DO you want the ASCII sequence of text? \nY or N\n')
if asci=='Y':
    asci1=[]
    for i in a:
        asci1.append(ord(i))
    print('The ascii sequence of text is: \n',asci1)
#TASK10= representing text in line format
print(' \n \n ')
line=input('DO you want to represent entered text in line formats? \nY or N\n')
if line=='Y':
    line1=input('This will break text in line format from the place of fullstops, you sure? \nY or N\n')
    if line1=='Y':
        line2=a.split('. ')
        print('The text becomes as: ')
        for i in line2:
            print(i,end='')
            print('.')
#TASK11= CApitalizing the whole text
#We have taken the hep of ascii table for the task
print(' \n \n ')
capitalise=input('Do you want to view the capitalise view of text? \nY or N\n')
if capitalise=='Y':
    capitalise1=''
    for i in a:
        if ord(i) in range(97,123):
            capitalise1=capitalise1+ chr(ord(i)-32)
        else:
            capitalise1=capitalise1+i
    print('The capitalized form of text is: \n',capitalise1)
#TASK12= doubling the gaps
'''doubling the gaps will provide ease to the users as on doubling the words it becomes easy
for us to carefully observe the words with more precision and will give less strain on eyes'''
print(' \n \n ')
doubling=input('Do you want to double the gaps between words? \nY or N\n')
if doubling=='Y':
    y=a.replace(' ','   ')
    print('The text becomes as: \n',y)
#TASK13= Text with only unique words
'''in this we will represent a text that will have only unique words of the given text
ex. word who is present more than once in the list then it will not be displayed  '''
print(' \n \n ')
unique=input('Do you want to see the unique form of the text? \nY or N\n')
if unique=='Y':
    unique1=''
    for i in b:
        count=0
        for j in c:
            if i==j:
                count+=1
        if count==1:
            unique1=unique1+i+' '
    print('The unique form of the text is: \n',unique1)
#TASK14= sorting text in descending order
print(' \n \n ')
desc=input('Do you want to sort the words in descending order? \nY or N\n')
if desc=='Y':
    desc1=[]
    for i in c:
        maxo=0
        for j in c:
            if j not in desc1:
                if len(j)>=maxo:
                    maxo=len(j)
                    maxo1=j
        desc1.append(maxo1)
    print('The descending order of words is as follows: ',desc1)
#TASK15= Capitalizing first alphabet of each word
print(' \n \n ')
capitalise_alpha=input('Do you want to capitalise the first letter of each word? \nY or N\n')
if capitalise_alpha=='Y':
    capi=a.split(' ')
    capi1=''
    for i in capi:
        if ord(i[0]) in range(97,123):
            capi1=capi1+chr(ord(i[0])-32)+i[1:]+' '
        else:
            capi1=capi1+i+' '
    print('The text becomes as: \n',capi1)
#TASK16= Finding words starting with the same alphabet
#suppose we find words that start with alphabet 'b'
print(' \n \n ')
same=input('Do you want to find the words starting with a particular alphabet? \nY or N\n')
if same=='Y':
    same1=input('Enter Alphabet in capital form: ')
    same2=[]
    for i in c:
        if i[0]==same1:
            same2.append(i)
        elif chr(ord(i[0])-32)==same1:
            same2.append(i)
    print('The words starting with the given alphabet are: ',same2)
#TASK17= words with max frequency
print(' \n \n ')
freq=input('Do you want to find the words most used in the text? \nY or N\n')
if freq=='Y':
    maxo=max(frequency1.values())
    freq1=[]
    for i in frequency1:
        if frequency1[i]==maxo:
            freq1.append(i)
    print('The word used max in the text is/are: ',freq1)
#TASK18= findind words of particular length
print(' \n \n ')
length=input('Do you want to find words of some particular length? \nY or N\n')
if length=='Y':
    length1=int(input('Enter the length of words which you want to find: '))
    length2=[]
    for i in c:
        if len(i)==length1:
            length2.append(i)
    print('Words with length ',length)
    print(length2)
