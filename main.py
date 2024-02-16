current_users = ['spooky', 'kitty', 'dicky', 'jizzy', 'ricky','kwabena']
new_users = ['spooky', 'kitty', 'Mdingo', 'drop', 'Kshot',"wabena"]
current_users_low = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users_low:
        print(f"The person will have to enter a new username {user}")
    else:
        print(f"The username {user} is available")



#
# for num in nums:
#     if something:
#         rwun code
#     else :
#         do another thing
#and , or

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    # print(num)
    else:
        print(num)