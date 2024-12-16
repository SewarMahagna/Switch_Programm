def get_char_frequencies(str): 
    dic_of_frequencies = {}
    for char in str:
        char = char.lower() if char.isalpha() else char
        if dic_of_frequencies.get(char):
            dic_of_frequencies[char] += 1  
        else:
            dic_of_frequencies[char] = 1  
    return dic_of_frequencies

def get_first_non_repeating_char(given_str):
    common_chars_dic = get_char_frequencies(given_str)
    for key in common_chars_dic : 
        if common_chars_dic.get(key) == 1 : 
            return key

str = "HHello My name is sewar"

print(get_first_non_repeating_char(str))