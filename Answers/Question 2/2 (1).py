
import numpy as np
import pandas as pd


a=input('Enter Name player1:')
b=input('player1 character:')
c=input('Enter Name player2:')
d=input('player2 character:')


if b=='s':
    print(a,'enter another character')
    b=input('player1 character')

if d=='s':
    print(c,'enter another character')
    d=input('player2 character')

if b==d:
    print(c,'enter another character')
    d=input('player2 character:')

print(a,'Character:',b)
print(c,'Character:',d)
rows=int(input('enter no. of rows:'))
col=int(input('enter no. of columns:'))
arr=np.zeros([rows,col])
df=pd.DataFrame(arr)
print(df)
num=rows*col
score1=0
score2=0

if num%2==0:
    num1=num/2+1
    i=1
    while i<num1:
        print('YOUR MOVE',a)
        choice=input('choose s/'+b+':')
        if choice!='s' and choice!=b:
            print('please enter correct characters')
            choice=input('choose s/'+b+':')
            
        e=int(input('enter row no.:'))
        f=int(input('enter col no.:'))
        if df.iat[e,f]!=0:
            print('position is filled! give different coordinates')
            e=int(input('enter row no.:'))
            f=int(input('enter col no.:'))
        df.iat[e,f]=choice
        print(df)
        print('YOUR MOVE',c)
        choice1=input('choose s/'+d+':')
        if choice1!='s' and choice1!=d:
            print('please enter correct characters')
            choice1=input('choose s/'+d+':')
        g=int(input('enter row no.:'))
        h=int(input('enter col no.:'))
        if df.iat[g,h]!=0:
            print('position is filled! give different coordinates')
            g=int(input('enter row no.:'))
            h=int(input('enter col no.:'))
        df.iat[g,h]=choice1
        print(df)
        i+=1

    for x in range (0,rows-2):
        for y in range (0,col-2):
            if df.iat[x,y]=='s' and df.iat[x,y+1]==b and df.iat[x,y+2]=='s':
                b=1
            
            if df.iat[x,y]=='s' and df.iat[x+1,y]==b and df.iat[x+2,y]=='s':
                b=1

            if df.iat[x,y]=='s' and df.iat[x+1,y+1]==b and df.iat[x+2,y+2]=='s':
                b=1

            if df.iat[x+2,y]=='s' and df.iat[x+1,y+1]==b and df.iat[x,y+2]=='s':
                b=1

            if b==1:
                score1+=1
    print('PLAYER1 SCORE:',score1)

    for x in range (0,rows-2):
        for y in range (0,col-2):
            if df.iat[x,y]=='s' and df.iat[x,y+1]==d and df.iat[x,y+2]=='s':
                b=1
            
            if df.iat[x,y]=='s' and df.iat[x+1,y]==d and df.iat[x+2,y]=="s":
                b=1

            if df.iat[x,y]=='s' and df.iat[x+1,y+1]==d and df.iat[x+2,y+2]=="s":
                b=1

            if df.iat[x+2,y]=='s' and df.iat[x+1,y+1]==d and df.iat[x,y+2]=='s':
                b=1

            if b==1:
                score2+=1

    print('PLAYER2 SCORE:',score2)


    if score1>score2 :
        print('PLAYER 1 WINS!')

    elif score2>score1:
        print('PLAYER 2 WINS')

    elif score1==score2:
        print('TIE')
else:
    print('p')
    p2=1
    num2=(num-1)/2
    while p2<=num2:
        print('YOUR MOVE',a)
        choice=input('choose s/'+b+':')
        if choice!='s' and choice!=b:
            print('please enter correct characters')
            choice=input('choose s/'+b+':')
        e=int(input('enter row no.:'))
        f=int(input('enter col no.:'))
        if df.iat[e,f]!=0:
            print('position is filled! give different coordinates')
            e=int(input('enter row no.:'))
            f=int(input('enter col no.:'))
            
        df.iat[e,f]=choice
        print(df)
        print('YOUR MOVE',c)
        choice1=input('choose s/'+d+':')
        if choice1!='s' and choice1!=d:
            print('please enter correct characters')
            choice1=input('choose s/'+d+':')
        g=int(input('enter row no.:'))
        h=int(input('enter col no.:'))
        if df.iat[g,h]!=0:
            print('position is filled! give different coordinates')
            g=int(input('enter row no.:'))
            h=int(input('enter col no.:'))
        df.iat[g,h]=choice1
        print(df)
        p2+=1
    print('YOUR MOVE',a)
    choice=input('choose s/'+b+':')
    if choice!='s' and choice!=b:
        print('please enter correct characters')
        choice=input('choose s/'+b+':')
    e=int(input('enter row no.:'))
    f=int(input('enter col no.:'))
    if df.iat[e,f]!=0:
            print('position is filled! give different coordinates')
            e=int(input('enter row no.:'))
            f=int(input('enter col no.:'))
    df.iat[e,f]=choice
    print(df)

    for x in range (0,rows-2):
        for y in range (0,col-2):
            if df.iat[x,y]=='s' and df.iat[x,y+1]==b and df.iat[x,y+2]=='s':
                b=1
            
            if df.iat[x,y]=='s' and df.iat[x+1,y]==b and df.iat[x+2,y]=='s':
                b=1

            if df.iat[x,y]=='s' and df.iat[x+1,y+1]==b and df.iat[x+2,y+2]=='s':
                b=1

            if df.iat[x+2,y]=='s' and df.iat[x+1,y+1]==b and df.iat[x,y+2]=='s':
                b=1

            if b==1:
                score1+=1
    print('PLAYER1 SCORE:',score1)

    for x in range (0,rows-2):
        for y in range (0,col-2):
            if df.iat[x,y]=='s' and df.iat[x,y+1]==d and df.iat[x,y+2]=='s':
                b=1
            
            if df.iat[x,y]=='s' and df.iat[x+1,y]==d and df.iat[x+2,y]=="s":
                b=1

            if df.iat[x,y]=='s' and df.iat[x+1,y+1]==d and df.iat[x+2,y+2]=="s":
                b=1

            if df.iat[x+2,y]=='s' and df.iat[x+1,y+1]==d and df.iat[x,y+2]=='s':
                b=1

            if b==1:
                score2+=1

    print('PLAYER2 SCORE:',score2)


    if score1>score2 :
        print('PLAYER 1 WINS!')

    elif score2>score1:
        print('PLAYER 2 WINS')

    elif score1==score2:
        print('TIE')




    

        


