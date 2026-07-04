unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class bomb:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds
    
Bomb1 = bomb(unlock_code, wire_color, seconds)

print(f"code : {Bomb1.unlock_code}")
print(f"color : {Bomb1.wire_color}")
print(f"second : {Bomb1.seconds}")