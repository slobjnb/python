# if语句
'''
cars = ['bmw','audi','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = '籍'
print(car=='籍')

age1 = 22
age2 = 10
print(age1 > 20 and age2 < 18)

numbers = ['1','2','6','6','5','4']
print('3' in numbers)
print('3' not in numbers)

car = 'subaru'
print("Is car == 'subaru'? I predict Tue")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false")
print(car == 'audi')

age = 12
if age < 4:
    print("You admisson cost is $0.")
elif age < 18:
    print("YOu admisson cost is $5.")
else :
    print("You admisson cost is $10.")

## 也可以使用多个 elif 省略 else

requested_topping = ['mushroom','extra cheese']
if 'mushroom' in requested_topping:
    print("Adding mushroom.")
if 'pepperion' in requested_topping:
    print("Adding pepperion.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
'

colors = ['green','yollow','red']
for color in colors:
    if color=='green':
        print("玩家获得5个点。")
'''       
food = []
if food:
    print("hhh.")
else:
    print("xxx.")

    
