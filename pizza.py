# 函数2
'''
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

def build_profile(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             filed = 'physics')
print(user_profile)
'''

def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)
