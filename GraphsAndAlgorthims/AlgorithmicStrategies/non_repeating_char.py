def get_char_frequencies(str): 
    count_dic = {}
    for char in str:
        char = char.lower() if char.isalpha() else char
        if count_dic.get(char):
            count_dic[char] += 1  
        else:
            count_dic[char] = 1  

    return count_dic

def get_first_non_repeating_char(given_str):
    common_chars_dic = get_char_frequencies(given_str)
    for key in common_chars_dic : 
        if common_chars_dic.get(key) == 1 : 
            return key

str = "HHello My name is sewar"

print(get_first_non_repeating_char(str))