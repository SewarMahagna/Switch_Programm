def largest_of_three(num1, num2, num3):
    largest = num1

    if num2 > largest:
        largest = num2
        
    if num3 > largest:
        largest = num3
        
    return largest