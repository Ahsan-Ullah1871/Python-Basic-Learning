#def squire(num):
#     return num*num
#
# print(squire(5))

def emojie_converter(text):
    words = text.split(" ")
    emojies = {
        ":)": "😁",
        "):": "😥",
        "^_~": "🤣"
    }

    output = ""
    for word in words:
        output += emojies.get(word, word) + " "
    return output

message = input("> ")
print(emojie_converter(message))