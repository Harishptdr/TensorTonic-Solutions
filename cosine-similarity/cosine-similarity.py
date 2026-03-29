import numpy as np

def cosine_similarity(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    
    dot_product = np.dot(a, b)
    magnitude = np.linalg.norm(a) * np.linalg.norm(b)
    
    if magnitude == 0:
        return 0.0  # avoid division by zero
    
    return dot_product / magnitude


# Test 1: Similar vectors
a = [1, 2, 3]
b = [1, 2, 3]
print("Identical vectors:", cosine_similarity(a, b))       # 1.0

# Test 2: Opposite vectors
a = [1, 0]
b = [-1, 0]
print("Opposite vectors:", cosine_similarity(a, b))        # -1.0

# Test 3: Perpendicular vectors
a = [1, 0]
b = [0, 1]
print("Perpendicular vectors:", cosine_similarity(a, b))   # 0.0

# Test 4: Random vectors
a = [1, 2, 3]
b = [4, 5, 6]
print("Random vectors:", cosine_similarity(a, b))          # 0.9746