M, D = map(int, input().split())

def find(M,D):
    if M==2:
        if 1<=D<=28:
            print("Yes")
        else:
            print("No")
    elif M%2!=0 and M<8:
        if 1<=D<=31:
            print("Yes")
        else:
            print("No")
    elif M%2==0 and M>=8:
        if 1<=D<=31:
            print("Yes")
        else:
            print("No")
    elif M==4 or M==6 or M==9 or M==11:
        if 1<=D<=30:
            print("Yes")
        else:
            print("No")
    else: 
        print("No")

find(M,D)