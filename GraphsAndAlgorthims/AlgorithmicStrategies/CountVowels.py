
vowels = {"A","a","E","e","I","i","O","o","U","u"}
def count_vowels(given_str): 
    vowels_counter = 0 
    const_count= 0
    for char in given_str : 
        if char.isalpha(): 
            if char in vowels:
                vowels_counter+=1
            else: 
                const_count += 1 
    print(f"The Number of vowels in - {given_str} is : {vowels_counter}")

str1= "Hello My Name Is Sewar"
str2 = "Vowel"
str3 = "Monday"

count_vowels(str1)
count_vowels(str2)
count_vowels(str3)