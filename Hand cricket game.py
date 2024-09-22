global count
global count2
count=0
count2=0
def batting(y=False):
    count=0
    while True:
        ch3=random.randint(0,10)
        ch4=int(input("Play your hand: "))
        if count>count2 and y==True:
            print("You have won by ",count-count2," runs!!")
        elif (ch3!=ch4!=0) and (ch3==0 and ch4==1 or ch3==ch1):
            print("u played -",ch4," oppn played-",ch3)
            print("Batsman out!")
            break
        else:
            print("u played -",ch4," oppn played-",ch3)
            count+=ch4
        print("You have scored: ",count)
    a=True
    bowling(a)
def bowling(y=False):
    count2=0
    while True:
        ch6=random.randint(0,10)
        ch7=int(input("Bowl : "))
        if (ch6!=ch7!=0) and (ch7==0 and ch6==1 or ch7==ch6):
            if count2==count and y==True:
                print("draw!!")
            else:
                print("u played -",ch7," oppn played-",ch6)
                print("out!!")
                break
        elif count<count2 and y==True:
            print("Batsman has won by ",count2-count," runs!!")
        else:
            print("u played -",ch7," oppn played-",ch6)
            count2+=ch6
    b=True
    batting(b)
print("LET'S PLAY HAND CRICKET!")
ch=input("Odd or Eve? : ")
if ch.lower()=="odd":
    ch1=int(input("enter ur choice toss : "))
    ch2=random.randint(0,10)
    print("u played -",ch1," oppn played-",ch2)
    if (ch1+ch2)%2!=0:
        ch5=input("Batting or Bowling? : ")
        if ch5.lower()=="batting":
            batting()
        else:
            bowling()
    else:
        choice=random.randint(1,2)
        if choice==1:
            print("oppn choose batting!!!")
            bowling()
        else:
            print("oppn choose bowling!!!")
            batting() 
