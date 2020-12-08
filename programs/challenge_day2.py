def string_calc(input):
    d = {"Upper":0, "Lower":0}
    for letter in input:
        if letter.isupper():
            d["Upper"]+=1
        elif letter.islower():
            d["Lower"]+=1
        else:
            pass
    
    return f'{input} \nUppercase: {d["Upper"]}\nLowercase: {d["Lower"]}'
    
print(string_calc("Hello world!"))