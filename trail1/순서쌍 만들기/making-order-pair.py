#와우 f포맷함수 잊고 있었는데 이런거였구나...

i=int(input())
 
for j in range(i,0,-1):
    for k in range(i,0,-1):
        print(f"({j},{k})", end=" ")
    print()