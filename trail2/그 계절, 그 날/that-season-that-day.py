Y, M, D = map(int, input().split())

def year(Y,M,D):
    if (Y%4==0 and Y%100!=0) or (Y%4==0 and Y%100==0 and Y%400==0): 
        return yoon(Y,M,D) 
    else:
        return just(Y,M,D) 

def yoon(Y,M,D):
    if M==2:
        if 1<=D<=29:
            return season(Y,M,D)
        else:
            return "-1"
    elif M%2!=0 and M<8:
        if 1<=D<=31:
            return season(Y,M,D)
        else:
            return "-1"
    elif M%2==0 and M>=8:
        if 1<=D<=31:
            return season(Y,M,D)
        else:
            return "-1"
    elif M==4 or M==6 or M==9 or M==11:
        if 1<=D<=30:
            return season(Y,M,D)
        else:
            return "-1"

def just(Y,M,D): 
    if M==2:
        if 1<=D<=28:
            return season(Y,M,D)
        else:
            return "-1"
    elif M%2!=0 and M<8:
        if 1<=D<=31:
            return season(Y,M,D)
        else:
            return "-1"
    elif M%2==0 and M>=8:
        if 1<=D<=31:
            return season(Y,M,D)
        else:
            return "-1"
    elif M==4 or M==6 or M==9 or M==11:
        if 1<=D<=30:
            return season(Y,M,D)
        else:
            return "-1"

def season(Y,M,D):
    if 3<=M<=5:
        return "Spring"
    elif 6<=M<=8:
        return "Summer"
    elif 9<=M<=11:
        return "Fall"
    elif 1<=M<=2 or M==12:
        return "Winter"

print(year(Y,M,D))