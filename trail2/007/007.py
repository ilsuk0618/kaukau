secret_code, meeting_point, time = input().split()
time = int(time)

class condi:
    def __init__(self,sc,mt,t):
        self.sc=sc
        self.mt=mt 
        self.t=t 

condi1=condi(secret_code,meeting_point,time)

print("secret code :",condi1.sc)
print("meeting point :",condi1.mt)
print("time :", condi1.t)