n=int(input())

class Distance:
    def __init__ (self, xp, yp, num):
        self.xp = xp
        self.yp = yp
        self.num = num
distances=[]

for i in range(n):
    xp, yp, num = tuple(map(int,input().split()))+(i+1,)
    distances.append(Distance(xp, yp, num))

distances.sort(key=lambda x : (abs(x.xp)+abs(x.yp)))

for distance in distances:
    print(distance.num)