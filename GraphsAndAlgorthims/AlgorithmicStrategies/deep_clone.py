def deepClone(obj):
    if obj is None or isinstance(obj, (int, float, str, bool)):
        return obj
    
    if isinstance(obj, list):
        return [deepClone(item) for item in obj]
    
    if isinstance(obj, dict):
        return {key: deepClone(value) for key, value in obj.items()}
    
    if isinstance(obj, set):
        return {deepClone(item) for item in obj}
    
    if isinstance(obj, tuple):
        return tuple(deepClone(item) for item in obj)

    raise TypeError(f"Object of type {type(obj)} is not supported")



x = {"a": "b", "a2": ["first", "second"]};
y = {"b": x, "b3": ["firtsY", x]};
z = deepClone(y);  

print("Original:", y)
print("Cloned:", z)  

z["b"]=[1,2]

print("Original after changing item in the cloned : ",y)
print("Cloned after changing item in the cloned : ",z)