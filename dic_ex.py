# input_numbers = input("digit_:")
# numers = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five"
# }
#
# output = ''
# for ch in input_numbers:
#      output += numers.get(ch,"!") + " "
# print(output)

# emoji converter

message = input(">")
words = message.split(" ")

emojies = {
    ":)":"😁",
    "):":"😥",
    "^_~":"🤣"
}

output = ""

for word in words:
    output += emojies.get(word,word) + " "
print(output)