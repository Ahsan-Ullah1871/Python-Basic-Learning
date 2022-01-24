secret_number = 4
try_time= 1

while try_time <=3:
    check = int(input("Enter Guess: "))
    try_time +=1
    if check == secret_number:
         print("You won!")
         break
else:
   print("You are fail!!")