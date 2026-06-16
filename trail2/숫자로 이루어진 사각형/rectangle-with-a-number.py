n = int(input())

def print_num(n):
    cnt=1
    for _ in range(n):
        for _ in range(n):
            if cnt==10:
                cnt=1
                print(cnt, end=" ")
                cnt+=1
            else:
                print(cnt, end=" ")
                cnt+=1
        print()

print_num(n)