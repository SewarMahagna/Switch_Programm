def get_char_frequencies(str): 
    dic_of_frequencies = {}
    for char in str:
        char = char.lower()
        if dic_of_frequencies.get(char):
            dic_of_frequencies[char] += 1  
        else:
            dic_of_frequencies[char] = 1  
    return dic_of_frequencies

def get_first_non_repeating_char(given_str):
    common_chars_dic = get_char_frequencies(given_str)
    for char in given_str : 
        if common_chars_dic.get(char.lower()) == 1 : 
            return char

str = "HHello MyyM nname is ssewar"

print(get_first_non_repeating_char(str))