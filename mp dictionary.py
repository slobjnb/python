# 字典
'''
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

del alien_0['points']
print(alien_0)

alien_0['speed'] = 'fast'
print(alien_0)

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print(favorite_languages)

friend = {'first_name':'王',
          'last_name':'小二',
          'age':'18',
          'city':'yuncheng'}
print(friend)

love_number = {'wang':'1',
               'li':'2',
               'duan':'3',
               'han':'4'}
print('love_number\n')

for name in love_number.keys():
    print(name)

pet_1 = {'name':'xx','kind':'hh','owner':'cc'}
pet_2 = {'name':'aa','kind':'ee','owner':'rr'}
pet = [pet_1,pet_2]
print(pet)

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
    
print('...')
for a in range(30):
    print(a)

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
'''

pizza = {
    'crust':'thick',
    'topping':['1','2','3']
    }
print(pizza)
















