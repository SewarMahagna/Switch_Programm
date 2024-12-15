def char_position(char):
    if char.isalpha():
        return ord(char.lower()) - ord('a') + 1
    return 0


def Word_Score(given_word): 
    if not given_word:
        return 0
    score = 0 
    for char in given_word : 
        score +=char_position(char) 
    return score

def Str_Score(given_str): 
    words_lst = given_str.split()
    highest_score = Word_Score(words_lst[0])
    max_word = words_lst[0]
    for word in words_lst :
        new_score = Word_Score(word)
        if new_score > highest_score : 
            highest_score = new_score
            max_word = word
    print(max_word)



str = "Happy Birthday"

Str_Score(str)


    