s=input()
l=s.split()
n=int(l[0])
m=int(l[1])
if n in range(5,101) and m in range(15,304):
    if n%2!=0 and m%2!=0:
        #for top
        for i in range(1,int(((n+1)/2))):
            x=m-(((2*i)-1)*3)
            x=int(x/2)
            print('-'*x,end='')
            print('.|.'*((2*i)-1),end='')
            print('-'*x)
        #for mid welcome
        w=m-7
        w=int(w/2)
        print('-'*w,end='')
        print('WELCOME',end='')
        print('-'*w)
        #for bottom
        for i in range(int(((n+1)/2))-1,0,-1):
            x=m-(((2*i)-1)*3)
            x=int(x/2)
            print('-'*x,end='')
            print('.|.'*((2*i)-1),end='')
            print('-'*x)

