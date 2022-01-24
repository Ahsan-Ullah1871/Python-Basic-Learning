
weight = input("Enter Your weight: ")
type = input("L(bs) Or (k)g: ")

if type.upper() == "L":
    print(f"Your are {float(weight)*0.45} kg")
elif type.upper() == "K":
    print(f"Your are {float(weight) // 0.45} pound")