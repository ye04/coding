userInput = input("Type what you want to translate into morse code! ")
userInput = userInput.lower()
result = []
for character in userInput:
    if character == "a":
        result.append(".- ")
    if character == "b":
        result.append("-... ")
    if character == "c":
        result.append("-.-. ")
    if character == "d":
        result.append("-.. ")
    if character == "e":
        result.append(". ")
    if character == "f":
        result.append("..-. ")
    if character == "g":
        result.append("--. ")
    if character == "h":
        result.append(".... ")
    if character == "i":
        result.append(".. ")
    if character == "j":
        result.append(".--- ")
    if character == "k":
        result.append("-.- ")
    if character == "l":
        result.append(".-.. ")
    if character == "m":
        result.append("-- ")
    if character == "n":
        result.append("-. ")
    if character == "o":
        result.append("--- ")
    if character == "p":
        result.append(".--. ")
    if character == "q":
        result.append("--.- ")
    if character == "r":
        result.append(".-. ")
    if character == "s":
        result.append("... ")
    if character == "t":
        result.append("- ")
    if character == "u":
        result.append("..- ")
    if character == "v":
        result.append("...- ")
    if character == "w":
        result.append(".-- ")
    if character == "x":
        result.append("-..- ")
    if character == "y":
        result.append("-.-- ")
    if character == "z":
        result.append("--.. ")
    if character == " ":
        result.append("/ ")


print(''.join(result))