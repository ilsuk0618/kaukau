arr=[input()
for _ in range(10)]
n=input()
cnt=0

for elem in arr:
    for i in range(len(elem)):
        if i==(len(elem)-1):
            if elem[i]==n:
                print(elem)
                cnt+=1
      
if cnt==0:
    print("None")
            
