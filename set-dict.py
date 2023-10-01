# 集合的運算
set1 = {3,4,5}
print(3 in set1)    # ()內為 True
print(7 in set1)    # ()內為 False
print(10 not in set1)    # ()內為 True
set2 = {4,5,6,7}
set3 = set1 & set2  # set3為set1, set2的交集
print(set3)     # >> {4,5}
set4 = set1 - set2  # set3為set1, set2的差集
print(set4)     # >> {3}

# 字典的運算
dict1 = {"apple":"蘋果", "bug":"蟲", "cat":"貓"}
print(dict1["apple"])  # >> 蘋果  
print("apple" in dict1)     # >> True
