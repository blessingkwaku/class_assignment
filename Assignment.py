current_users=['prince','john','angela']
new_users=['raymond','godson','john']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to enter a new name")
    else:
        print("User name is available")
        
numbers= list(range(1,101))
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)