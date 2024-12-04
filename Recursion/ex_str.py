#Permutations of a String
#- Problem: Write a function to generate all possible permutations of a given string. 
#- Example Input: permutations("abc") 
#- Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']'

def string_permutations(input_string):
    
    if len(input_string) == 1:
        return [input_string]
    
    permutations_lst = []
    for i , char in  enumerate(input_string) : 
        str_without_i = input_string[:i] + input_string[i+1:]
        for p in string_permutations(str_without_i):
            permutations_lst.append(char + p)
    return permutations_lst
            
result=string_permutations("abc")
print(result)
