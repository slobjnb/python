# 列表2

motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

# 末尾添加 append
motorcycle.append('honda')
print(motorcycle)

# 列表中添加 insert
motorcycle = ['honda','yamaha','suzuki']
motorcycle.insert(0,'dukati')
print(motorcycle)

# 已知位置，删除 del
print(motorcycle)
del motorcycle[0]
print(motorcycle)

# 弹出末尾的元素 pop
print(motorcycle)
popped_motorcycle = motorcycle.pop()
print(popped_motorcycle)

# 弹出列表中任意位置的元素 pop()
motorcycle = ['honda','yamaha','suzuki']
first_cycle = motorcycle.pop(0)
print('The first motorcycle was a '+first_cycle+'.')
print(motorcycle)

# 根据值删除元素 remove()
motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
motorcycle.remove('honda')
print(motorcycle)

# 练习
names = ['李','王','唐']
print('请你来参加我的宴会—'+names[0]+'。')
print('请你来参加我的宴会—'+names[1]+'。')
print('请你来参加我的宴会—'+names[2]+'。')
print('很抱歉，我没办法来参加你的宴会-'+names[0]+'。')
names[0] = '张'
print('请你来参加我的宴会—'+names[0]+'。')
names.append('侯')
names.append('安')
names.append('籍')
print(names)
print('我找到一张更大的桌子，请你来-'+names[3]+'。')
print('我找到一张更大的桌子，请你来-'+names[4]+'。')
print('我找到一张更大的桌子，请你来-'+names[5]+'。')
names.insert(2,'赵')
names.insert(0,'胡')
print(names)
popped_1 = names.pop(0)
print('很抱歉-'+popped_1+'。')
popped_1 = names.pop(0)
popped_1 = names.pop(0)
popped_1 = names.pop(0)
popped_1 = names.pop(0)
print(names)
del names[0]
del names[1]
print(names)
del names[0]
print(names)











