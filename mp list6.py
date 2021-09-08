## 数字列表
'''
for value in range(1,5):
    print(value)
number = list(range(1,6))
print(number)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))    

squares = [value**2 for value in range(1,11)]
print(squares)

for nb in range(1,21):
    print(nb)

nb1 = [value for value in range(1,1000001)]
print(nb1)
print(sum(nb1))
'''
number = [value for value in range(1,10,2)]
print(number)

