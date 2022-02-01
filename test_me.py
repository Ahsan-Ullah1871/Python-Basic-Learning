

def find_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
         if number%2 == 0:
            find_event = number
            even_numbers.append(number)
    return even_numbers


print(find_even_numbers([12,4,5,6,8,9]))