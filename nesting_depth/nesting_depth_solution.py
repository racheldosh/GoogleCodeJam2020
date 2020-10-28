input_file = open("input.txt", "r")
num_test_cases = int(input_file.readline())

"""
Nesting depth

Given a string, outputs a string with 'a minimum number of opening and closing parentheses 
such that the resulting string is balanced and each digit d is inside exactly d pairs of 
matching parentheses.'
"""
for test_case in range(1, num_test_cases + 1):
    string = input_file.readline()
    result = ""
    num_open_parentheses = 0

    for char in string.rstrip():
        int_char = int(char)
        if int_char == 0:
            # when we reach a zero, we need to close all the parentheses first
            # since the character zero must be surrounded by zero parentheses
            while num_open_parentheses > 0:
                result += ")"
                num_open_parentheses -= 1
            result += "0"

        if int_char > 0:
            # if we don't have enough open parentheses, we need to first add
            # as many open parentheses as needed
            if num_open_parentheses < int_char:
                while num_open_parentheses < int_char:
                    result += "("
                    num_open_parentheses += 1
            # if we have too many open parentheses, we need to first close
            # as many closed parentheses as needed
            elif num_open_parentheses > int_char:
                while num_open_parentheses > int_char:
                    result += ")"
                    num_open_parentheses -= 1
            result += char
    # lastly, we need to close all remaining parentheses
    result += (num_open_parentheses * ")")
    print("Case #{}: {}".format(test_case, result))