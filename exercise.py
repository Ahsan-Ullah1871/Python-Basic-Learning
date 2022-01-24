numbers = [1,1,2,2,3,3,4,5,6,7]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)