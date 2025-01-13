#o(nlog(n))
def is_anagrams(str1,str2): 
    if len(str1)!=len(str2):
        return False
    
    arranged_str1 = sorted(arranged_str1.lower())
    arranged_str2 = sorted(arranged_str2.lower())

    return arranged_str1 == arranged_str2

#o(n)
def count_common(arr): 
    count_dic = {}
    for element in arr:
        if count_dic.get(element):
            count_dic[element] += 1  
        else:
            count_dic[element] = 1  
    return count_dic

def is_anagram(str1,str2): 
    if len(str1)!=len(str2):
        return False
    
    str1_commons_dic = count_common(str1.lower()) # Hello {"h" : 1}
    str2_commons_dic = count_common(str2.lower())

    for key in str1_commons_dic:
        if str1_commons_dic.get(key, 0) != str2_commons_dic.get(key, 0):
            return False

    for key in str2_commons_dic:
        if str2_commons_dic.get(key, 0) != str1_commons_dic.get(key, 0):
            return False

    return True

"""print(is_anagram("silent","listen"))
print(is_anagram("abc","cba"))
print(is_anagram("Heart","Earth"))
print(is_anagram("oHell","Hell"))
print(is_anagram("test","TEsst"))"""




