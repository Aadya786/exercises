vectors = {
    "apple": [7, 2],
    "lemon": [2, 9],
    "banana": [9, 1],
    "grape": [6, 3]
}

def distance(v1, v2):
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    return dx*dx + dy*dy 

def findclosest(target_vector):
    best_fruit = None
    best_distance = float("inf")

    for fruit, vector in vectors.items():
        d = distance(target_vector, vector)
        if d < best_distance:
            best_distance = d
            best_fruit = fruit

    return best_fruit

user_input = input("Enter a sweet and sour ratio (seperated by a space): ")
parts = user_input.split()
sweet = int(parts[0])
sour  = int(parts[1])
target = [sweet, sour]
closest = findclosest(target)

print("The closest fruit is:", closest)
