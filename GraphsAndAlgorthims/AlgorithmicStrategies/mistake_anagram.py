from collections import Counter
def is_1_mistake_anagram(str1,str2):    
    str1_commons_dic = Counter(str1.lower())
    str2_commons_dic = Counter(str2.lower())
    mistake_counter1 = 0 
    mistake_counter2 = 0 

    for key in str1_commons_dic:
        if str1_commons_dic.get(key, 0) != str2_commons_dic.get(key, 0):
            mistake_counter1 +=1
        if mistake_counter1 > 1:
            return False

    for key in str2_commons_dic:
        if str2_commons_dic.get(key, 0) != str1_commons_dic.get(key, 0):
            mistake_counter2 +=1 

        if mistake_counter2 > 1:
            return False

    return (mistake_counter2 == 1 or mistake_counter1==1 )

print(is_1_mistake_anagram("ab","abc"))
print(is_1_mistake_anagram("Sewar","Sewa"))
print(is_1_mistake_anagram("Hello","LEloh"))
print(is_1_mistake_anagram("heart","Earth"))
print(is_1_mistake_anagram("abc","cna"))