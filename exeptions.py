try:
    age = int(input("Age: "))
    life_income = 20000000
    total_income = life_income / age
    print(age)
except ZeroDivisionError:
    print("O can not be age of any animal 😶")
except ValueError:
    print("Invalid value")