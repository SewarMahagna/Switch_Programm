def if_str_is_rotation(original_str, rotation_str):
    if len(original_str) != len(rotation_str) or not original_str:
        return False
    
    first_letter = original_str[0]
    possible_indices = [i for i, char in enumerate(rotation_str) if char == first_letter]
    
    for index in possible_indices:
        first_section = rotation_str[:index]
        second_section = rotation_str[index:]
        new_rotation = second_section + first_section
        
        if new_rotation == original_str:
            return True
    
    return False

def effecient_alg(original_str,rotation_str):
    if len(original_str) != len(rotation_str):
            return False

    new_str= original_str + original_str
    if rotation_str in new_str:
        return True 
    return False

test_cases = [
    ("abc", "cab"),      # True
    ("abc", "bca"),      # True
    ("hello", "llohe"),  # True
    ("hello", "ohell"),  # True
    ("abc", "cba"),      # False
    ("", ""),            # False
    ("a", "a"),          # True
    ("aa", "aa"),        # True
]

for original, rotation in test_cases:
    result = effecient_alg(original, rotation)
    print(result)

