size=int(input())
if size in range(1,27):
    l=(4*size)-3
    #for top
    for i in range(1,size+1):
        d=l-((4*i)-3)
        d=int(d/2)
        print('-'*d,end='')
        s=''
        a=size-(i-1)
        alp=size-a
        for j in range(alp+a,a,-1):
            s+=chr(j+96)+'-'
        s+=chr(a+96)
        for j in range(a+1,alp+a+1):
            s+='-'+chr(j+96)
        print(s,end='')
        print('-'*d)
    #for bottom
    for i in range(2,size+1):
        alp=size-i
        d=l-((4*alp)+1)
        d=int(d/2)
        print('-'*d,end='')
        s=''
        for j in range(i+alp,i,-1):
            s+=chr(j+96)+'-'
        s+=chr(i+96)
        for j in range(i+1,alp+i+1):
            s+='-'+chr(j+96)
        print(s,end='')
        print('-'*d)