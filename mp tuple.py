## 元组

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)
'''
## 错误指令，元组无法修改，可重新定义
dimensions[0]=200
'''

dimensions = (1,2)
for dimension in dimensions:
    print(dimension)
