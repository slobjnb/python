# 函数

'''
def greet_user():
    print("hello!")
greet_user()

def greet_user(username):
    print("hello "+username+"!")
greet_user('jnb')

def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("my"+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')
describe_pet('dog','willie')


def get_formatted_name(first_name,last_name):
    full_name = first_name + ' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

def bulid_person(first_name,last_name,age = ''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = bulid_person('jimi','hendrix',age = 27)
print(musician)

def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First_name: ")
    if f_name =='q':
        break
    l_name = input("Last_name")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nhello, "+formatted_name+"!")
'''
def greet_users(names):
    for name in names:
        msg = "Hello "+name.title()+"!"
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)


















    
