temp = 30

# if temp > 30:
#     print("It's hot day")
# else:
#     print("Its not a hot day")


#
name =input("Enter your name")

if len(name) <= 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks fine!")