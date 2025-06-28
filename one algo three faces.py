def detect_collection(obj):
    # Strict type check (exact match)
    if type(obj) is list:
        return "list (exact type)"
    elif type(obj) is tuple:
        return "tuple (exact type)"
    elif type(obj) is set:
        return "set (exact type)"
    
    # isinstance allows inheritance/subclasses
    if isinstance(obj, list):
        return "list (or subclass)"
    elif isinstance(obj, tuple):
        return "tuple (or subclass)"
    elif isinstance(obj, set):
        return "set (or subclass)"
    
    return "Not a list, tuple, or set"

# Examples
examples = [
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    "hello",
]

for x in examples:
    print(f"{x!r} → {detect_collection(x)}")
