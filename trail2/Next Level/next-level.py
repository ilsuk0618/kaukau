user2_id, user2_level = input().split()
user2_level = int(user2_level)

class info:
    def __init__(self,id="codetree",lev="10"):
        self.id=id
        self.lev=lev
info1 = info()
info2 = info(user2_id,user2_level)

print("user", info1.id, "lv", info1.lev)
print("user", info2.id, "lv", info2.lev)