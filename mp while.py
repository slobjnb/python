# while
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

while True:
    number = input("Please input:")
    print(number)
    if number == 'nb':
        break
    
current_number = 0
while current_number < 10:
    current =+ 1
    if current_number % 2 == 0:
        continue
    print(current_number)

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is you name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
        
print("\n---Poll Results---")
for name,response in responses.items():
    print(name+"would like to climb "+response+".")
'''

a = ['1','2','3','4']
b = []
while a:
    c = a.pop()
    print("number:"+c)
    b.append(c)
print("number2:")
for number in b:
    print(number)
    
