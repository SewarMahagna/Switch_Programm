def print_repeated_chars(given_str):

    prev_char = given_str[0]
    output_str=""
    count_current_char = 0

    for char in given_str:
        if char != prev_char : 
            output_str = output_str+prev_char+str(count_current_char)
            prev_char = char
            count_current_char = 1
        else : 
            count_current_char+=1

    output_str = output_str+prev_char+str(count_current_char)
    print(output_str)

str_1 = "aaaabbcbabb"

print_repeated_chars(str_1)

        

            