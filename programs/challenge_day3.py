def zip(input1, input2):
    if len(input1) == len(input2):
        output = ""
        for i in range(len(input1)):
            output += input1[i] + input2[i]
        return output
    else:
        return "Input two Strings of equal length."

print(zip("String", "Fridge"))
print(zip("Dog", "Cat"))
print(zip("True", "Tre4"))
print(zip("True", "QACommunity"))
