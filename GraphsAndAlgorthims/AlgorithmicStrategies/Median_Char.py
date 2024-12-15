def Median_char(given_str): 
    if not given_str:
        return None 
    
    ascii_val = [ord(char) for char in given_str]
    sorted_ascii_val = sorted(ascii_val)
    n = len(sorted_ascii_val)  
    if n%2 ==0 : 
        return chr(sorted_ascii_val[n//2 - 1])
    return chr(sorted_ascii_val[n//2])


str1 = "question"

print(Median_char(str1))