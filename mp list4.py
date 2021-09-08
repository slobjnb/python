# 列表4

# 永久排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 临时排序
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print(cars)

# 倒着打印(并不是倒着排序，只是反转原来的排列顺序)
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

# 列表的长度

cars = ['bmw','audi','toyota','subaru']
len(cars)
print(len(cars))

# 练习

places = ['b','x','a','e','u']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
len(places)
print(len(places))

text = ['山','水','木','土','火']
print(text)
print(sorted(text))

text = ['籍','赵','玩','唐','若','含']
print(text)
print(sorted(text))


