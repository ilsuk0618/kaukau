num=int(input())
arr=map(float,input().split())
score=sum(arr)
avg=score/num
   
if avg>=4.0:
     print(f"{avg:.1f}")
     print("Perfect")
elif avg>=3.0 and avg<4.0:
     print(f"{avg:.1f}")
     print("Good")
else:
     print(f"{avg:.1f}")
     print("Poor")