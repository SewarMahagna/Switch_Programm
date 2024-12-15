
vowels = ["A","a","E","e","I","i","O","o","U","u"]
def count_vowels(given_str): 
    counter = 0 
    for char in given_str : 
        if char in vowels:
            counter+=1 
    print(f"The Number of vowels in - {given_str} is : {counter}")

str1= "Hello My Name Is Sewar"
str2 = "Vowel"
str3 = "Monday"

count_vowels(str1)
count_vowels(str2)
count_vowels(str3)