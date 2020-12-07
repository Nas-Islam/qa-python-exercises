def sort_alph(input):
    output_string = ""
    input_list = input.split()
    ## Create a dictionary, using the words from the list as keys. This removes duplicates because dictionaries cannot have duplicate keys.
    ## Then convert dictionary back into a list
    input_list = list(dict.fromkeys(input_list))
    sorted_list = sorted(input_list)

    for i in range(len(sorted_list)):
        output_string += sorted_list[i] + " "
    return output_string

print(sort_alph("hello world and practice makes perfect and hello world again"))
