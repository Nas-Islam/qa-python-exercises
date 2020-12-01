basic_nums = {1:'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
phrase_nums = ['Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 
'Eighty', 'Ninety', 'Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion']
numtowordsString = []
def numtoword(number):
    num_list = [int(d) for d in str(number)]
    if number == 0:
        print("Zero")
    ## 
    elif len(num_list) >= 7:
        if len(num_list % 3 == 0):
            numtowordsString.append(basic_nums[num_list(i)])
    return num_list

print(numtoword(123))
print(len(numtoword(123)))