"""
Given a string s and a dictionary of strings wordDict
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
"""
def is_word_break(givenStr, wordDict):

    min_word_len = min(len(word) for word in wordDict)  
    constructed_str = ""
    if len(givenStr) < min_word_len:
        return False

    index = 0
    while index < len(givenStr):
        match_found = False  
        for word in wordDict:
            word_len = len(word)
            sub_str = givenStr[index:index + word_len]
            if word == sub_str:  
                constructed_str += word
                index += word_len
                match_found = True
                break  

        if not match_found:
            return False

    return constructed_str == givenStr

print(is_word_break("applepenapple", ["apple","pen"])) #True
print(is_word_break("applepenapple", ["apples","apple","pen"])) #True
print(is_word_break("leetcode",["leet","code"])) #True
print(is_word_break("catsandog",["cats","dog","sand","and","cat"])) #False
print(is_word_break("pineapplepenapple",  ["apple", "pen", "applepen", "pine", "pineapple"]))  # True
print(is_word_break("dogsandcat", ["dog", "sand", "cat"])) #True
print(is_word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])) #True