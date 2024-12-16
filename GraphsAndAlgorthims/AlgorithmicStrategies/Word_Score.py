def get_char_score(char):
    if char.isalpha():
        return ord(char.lower()) - ord('a') + 1
    return 0


def get_word_score(given_word): 
    if not given_word:
        return 0
    score = 0 
    for char in given_word : 
        score +=get_char_score(char) 
    return score

def get_max_word_score(given_str): 
    words_lst = given_str.split()
    max_score = get_word_score(words_lst[0])
    max_word = words_lst[0]

    for word in words_lst :
        new_score = get_word_score(word)
        if new_score > max_score : 
            max_score = new_score
            max_word = word

    print(max_word)



str = "Happy Birthday"

get_max_word_score(str)


    