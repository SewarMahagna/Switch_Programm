def char_position(char):
    if char.isalpha():
        return ord(char.lower()) - ord('a') + 1
    return 0

def Word_Score(given_word): 
    if not given_word:
        return 0
    return sum(char_position(char) for char in given_word)

def Str_Score(given_str): 
    words_lst = given_str.split()
    max_word = max(words_lst, key=Word_Score)
    print("The word with max score is : ", max_word)


str = "Hello from python "

Str_Score(str)


    