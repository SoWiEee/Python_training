# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((self.x-targetX)**2 + (self.y-targetY)**2)**0.5

p=Point(3,4)
p.show()    # 呼叫實體方法（本質是函式）
result=p.distance(0,0)     # 計算座標3,4 和 座標0,0的距離
print(result)

# 建立第一個實體物件
p1=Point(3,4)
print(p1.x, p1.y)

# 建立第二個實體物件
p2=Point(5,6)
print(p2.x, p2.y)

# FullName 實體物件的設計：分開紀錄姓、名資料的全名
class FullName():
    def __init__(self, first, last):
        self.first=first
        self.last=last

name1=FullName("C.W.", "Peng")
print(name1.first, name1.last)

name2=FullName("T.Y.", "Lin")
print(name2.first, name2.last)

# File 實體物件的設計：包裝檔案讀取的格式
class File:
    def __init__(self, name):
        self.name=name
        self.file=None  # 尚未開啟檔案，初期是None
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()

f1=File("data1.txt")
f1.open()



