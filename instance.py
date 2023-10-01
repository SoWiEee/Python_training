# Point 實體物件：平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# 建立實體物件p1, p2
p1 = Point(2,6)
print(p1.x, p1.y)   # >> 2 6
p2 = Point(3,4)
print(p2.x, p2.y)   # >> 3 4

# FullName 實體物件：分開紀錄姓,名
class FullName:
    def __init__(self):
        self.fir = "C.W"
        self.las = "Peng"

name1 = FullName()
print(name1.fir,name1.las)  # >> C.W Peng

