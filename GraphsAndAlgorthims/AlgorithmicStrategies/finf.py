def add(num1,num2='not assigned'):
    if isinstance(num2,int)  and isinstance(num1,int):
        result = num1+num2
        return result
    else:
        def result_f(num=0):
            return num + num1
        return result_f





print(add(2,5))
print(add(2)())
print(add(2)(5))
